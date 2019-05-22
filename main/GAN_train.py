import torch
from torch.autograd import Variable
from data.data_loader import CreateDataLoader
from models.models2 import create_model
from options.train_options import TrainOptions
# parser = argparse.ArgumentParser(description='Train PIX2PIxHD GAN')
# parser.add_argument('--gan_path', help="path to gan model")
# parser.add_argument('--train_path', help="path to train set frames")
# parser.add_argument('--checkpoint', help="to save model weights at different checkpoints")
# args = parser.parse_args()

opt = TrainOptions().parse()
# print(type(opt))

##### Change the options to match pose specific
opt.dataroot = 'C:/Users/Damini/PycharmProjects/BME_Project/project_BME/train'
opt.checkpoints_dir = "C:/Users/Damini/PycharmProjects/BME_Project/project_BME/data"
opt.display_freq = 640 # TODO: change to  1 WHEN debugging
opt.display_winsize = 512 # TODO: Chnage with img size
opt.lambda_feat = 8.0 # Tried 10, 8 better than 10
opt.loadSize = 512
opt.lr=0.0004
opt.name = 'train'
# ndf = #no filters to start with Discriminator
opt.ndf = 64
opt.niter = 5
opt.niter_decay = 5
opt.no_instance = True
opt.phase = 'train'
opt.print_freq = 640
opt.save_latest_freq = 640

if __name__ == '__main__':

    dataloader = CreateDataLoader(opt)
    dataset = dataloader.load_data()
    dataset_size = len(dataloader)
    stop_epoch = 10
    epoch_iter = 0
    disp = epoch_iter % opt.display_freq
    model = create_model(opt)
    for epoch in range(1, stop_epoch):
        for i, data in enumerate(dataset, start=epoch_iter):
            epoch_iter += opt.batchSize
            fake = epoch_iter % opt.display_freq == disp
            losses, _ = model(Variable(label_map=data['label']), real_image=data['image'], inst_map=data['inst'], feat_map=data['feat'], infer=fake)

            losses = [torch.mean(i) if not isinstance(i, int) else i for i in losses]
            # easier to specify loss for GAN and discriminator
            loss_dict = dict(zip(model.module.loss_names, losses))
            LD = (1/2) * (loss_dict['D_fake'] + loss_dict['D_real'])
            LG = loss_dict.get('G_GAN_Feat', 1) + loss_dict.get('G_VGG', 1) + loss_dict['G_GAN']

            model.module.optimizer_D.zero_grad()
            model.module.optimizer_G.zero_grad()
            # back prop
            LD.backward()
            LG.backward()
            # update
            model.module.optimizer_D.step()
            model.module.optimizer_G.step()

    model.module.save('best')

