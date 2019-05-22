import os
import argparse
import imageio

parser = argparse.ArgumentParser(description='ADD Frames as train2/test data')
parser.add_argument('--test_path', help="path to test images")
parser.add_argument('--train_path', help="path to train images")
args = parser.parse_args()

if __name__ == '__main__':
    if len(os.listdir(args.test_path)) == len(os.listdir(args.train_path)):
        test_images = []
        for file_name in os.listdir(args.test_path):
            # print(file_name)
            if file_name.endswith('.jpg'):
                file_path = os.path.join(args.test_path, file_name)
                test_images.append(imageio.imread(file_path))
        imageio.mimsave('chachi_test_pose.gif', test_images)

        train_images = []
        for file_name in os.listdir(args.train_path):
            # print(file_name)
            if file_name.endswith('.jpg'):
                file_path = os.path.join(args.train_path, file_name)
                train_images.append(imageio.imread(file_path))
        imageio.mimsave('chachi_test_pose.gif', train_images)
    else:
        print('make sure the number of images in test and train are the same')

