import cv2
import torch
from network.rtpose_vgg import get_model, use_vgg
from evaluate.coco_eval import get_multiplier, get_outputs, handle_paf_and_heat
from openpose_utils import get_pose
from network.post import decode_pose
import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser(description='Generate Poses')
parser.add_argument('--train_path', help="path to train set frames")
parser.add_argument('--test_path', help="path to test set frames")
args = parser.parse_args()

train = Path(args.train_path)
test = Path(args.test_path)
if not os.path.exists(train.joinpath('train_label')):
    os.makedirs(train.joinpath('train_label'))

if not os.path.exists(test.joinpath('test_label')):
    os.makedirs(test.joinpath('test_label'))


if __name__ == '__main__':

    train_pose_dir = train.joinpath('train_label')
    test_pose_dir = test.joinpath('test_label')
    model = get_model(trunk='vgg19')
    model_path = 'pose_model_scratch.pth'
    model = torch.nn.DataParallel(model).cuda()
    model.load_state_dict(torch.load(model_path))
    model.eval()

    for idx in range(200, 210):
        train_img_path = train.joinpath('train_set')
        train_img_name = "image%0d.jpg" % idx
        train_img_path = train_img_path.joinpath(train_img_name)
        train_image = cv2.resize( cv2.imread(str(train_img_path)), (512, 512))
        train_multiplier = get_multiplier(train_image)

        test_img_path = test.joinpath('test_set')
        test_img_name = "image%0d.jpg" % idx
        test_img_path = test_img_path.joinpath(test_img_name)
        test_image = cv2.resize( cv2.imread(str(test_img_path)), (512, 512))
        test_multiplier = get_multiplier(test_image)

        with torch.no_grad():
            train_paf, train_heatmap = get_outputs(train_multiplier, train_image, model, 'rtpose')
            test_paf, test_heatmap = get_outputs(test_multiplier, test_image, model, 'rtpose')

            # use [::-1] to reverse!
            train_swapped_img = train_image[:, ::-1, :]
            test_swapped_img = test_image[:, ::-1, :]


            train_flipped_paf, train_flipped_heat = get_outputs(train_multiplier, train_swapped_img, model, 'rtpose')
            test_flipped_paf, test_flipped_heat = get_outputs(test_multiplier, test_swapped_img, model, 'rtpose')

            train_paf, train_heatmap = handle_paf_and_heat(train_heatmap, train_flipped_heat, train_paf, train_flipped_paf)
            test_paf, test_heatmap = handle_paf_and_heat(test_heatmap, test_flipped_heat, test_paf, test_flipped_paf)


        param = {'thre1': 0.1, 'thre2': 0.05, 'thre3': 0.5}
        train_pose = get_pose(param, train_heatmap, train_paf)
        test_pose = get_pose(param, test_heatmap, test_paf)
        pose_name = "pose%0d.jpg" % idx
        cv2.imwrite(str(test_pose_dir.joinpath(pose_name)), test_pose)
        cv2.imwrite(str(train_pose_dir.joinpath(pose_name)), train_pose)

