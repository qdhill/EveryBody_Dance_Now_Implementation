import os
import torch
import cv2
from data.data_loader import CreateDataLoader
from models.models2 import create_model
import util.util2 as util
from options.test_options import TestOptions
torch.backends.cudnn.benchmark = False
if __name__ == '__main__':

    opt = TestOptions().parse(save=False)
    print(opt)
    opt.results_dir ='C:/Users/Damini/PycharmProjects/BME_Project/project_BME/data/generated_path'
    opt.nThreads = 1
    opt.no_instance = True
    opt.batchSize = 1
    opt.phase = 'test'
    opt.serial_batches = True
    opt.no_flip = True
    opt.checkpoints_dir = 'C:/Users/Damini/PycharmProjects/BME_Project/project_BME/data/'
    opt.dataroot = 'C:/Users/Damini/PycharmProjects/BME_Project/project_BME/data/test'
    data = 'C:/Users/Damini/PycharmProjects/BME_Project/project_BME/data'
    opt.which_epoch='best'

    opt.label_nc = 18
    opt.loadSize = 512
    opt.name='weights'

    model = create_model(opt)
    dataloader = CreateDataLoader(opt)
    dataset = dataloader.load_data()
    dataset_size = len(dataloader)

    if not os.path.exists(opt.results_dir):
        os.makedirs(opt.results_dir)

    for idx, data in enumerate(dataset):
        generated = model.inference(data['label'], data['inst'])
        img_path = data['path']
        name = "generated%0d.jpg" % idx
        img_path = opt.results_dir + '/' + name
        cv2.imwrite(img_path, util.tensor2im(generated.data[0]))



