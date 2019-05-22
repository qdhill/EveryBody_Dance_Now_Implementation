import cv2
import os
import shutil
import argparse

parser = argparse.ArgumentParser(description='ADD Frames as train2/test data')
parser.add_argument('--path', help="path to video to generate frames")
parser.add_argument('--save_path', help="path to store saved frames as train2/test set")
args = parser.parse_args()


vid = cv2.VideoCapture(args.path)
if os.path.exists(args.save_path):
    shutil.rmtree(args.save_path)

os.makedirs(args.save_path)

success, image = vid.read()
count = 0
start = 200
stop  = 210
while success:
    print(count)
    success, image = vid.read()
    if count >= start and count <= stop:
        name = "image%0d.jpg" % count
        save_path_name = args.save_path + '/' + name
        print(save_path_name)
        cv2.imwrite(save_path_name, image)
    if count > stop:
        break

    count += 1



