from .utils import data_utils
from .utils import model_utils
from .models import vgg_face


def train_model(train_X_path,train_y_path,test_X_path,test_y_path,version="Mega",batch_size=16,num_epochs=50,model_name="VGG-face"):

    device= torch.device("cuda")
    channels = 3
    img_pixels = (224,224)
    lr = 0.001
    # num_epochs = 50
    # batch_size = 16
    transform = transforms.Compose([
        transforms.Resize(img_pixels),
        transforms.ToTensor()])

    print("[+] This training pipeline is for demo usage")
    for binsize in [1]:
        classes = int((100 + binsize - 1) / binsize)
        samples=np.load(train_X_path)
        labels=np.load(train_y_path)
        testsamples=np.load(test_X_path)
        testlabels=np.load(test_y_path)
        dataloaders={}
        dataloaders['train'] = data_utils.make_dataloader(samples,labels,img_size=img_pixels,batch_size=batch_size,transform_test=transform,shuffle=True)
        dataloaders['test'] = data_utils.make_dataloader(testsamples,testlabels,img_size=img_pixels,batch_size=batch_size,transform_test=transform,shuffle=True)
    
        for model in ["MLP", "ResNet", "VGG"]:
            print("[+] Training for %s with binsize %d dataset started" % (model, binsize))
        
            if model == "MLP":
            # net = MLP(channels * img_pixels[0] * img_pixels[1], 512, 512, 512, 512, classes)
                continue
            elif model == "ResNet":
            # net = resnet18(num_classes=classes)
            # comment this as this is a demo
                continue
            else:
                net = VGG_16(classes=classes)
            # net.load_weights()
            # comment this as this is a demo
            # continue
        
            model_save_name = "%s_%s_demo_merged_train_bin%d" % (num_epochs, net.__class__.__name__, binsize)
            model_utils.training_and_save_model(net, num_epochs, model_save_name)

            print("[+] Training for %s with binsize %d dataset done" % (model, binsize))

            del net 


if __name__=="__main__":

    parser = argparse.ArgumentParser(description='control experiment')

    parser.add_argument('-folder', help='base folder',
                        default='datasets')
    parser.add_argument('-train_X_path', help='training samples', default='Mega_train_x.npy')
    parser.add_argument('-train_y_path', help='training labels', default='Mega_train_y.npy')
    parser.add_argument('-test_X_path', help='test samples', default='Mega_test_x.npy')
    parser.add_argument('-test_y_path', help='test labels', default='Mega_train_y.npy')
    parser.add_argument('-model_name', help='model to be trained', default='VGG-face')
    parser.add_argument('-version', help='version_of_model', default='Mega')
    parser.add_argument('-num_classes', type=int, help='number of classes', default=10)

    args = parser.parse_args()
    train_X_path = os.path.join(args.folder, args.train_X_path)
    train_y_path = os.path.join(args.folder, args.train_y_path)
    test_X_path = os.path.join(args.folder, args.test_X_path)
    test_y_path = os.path.join(args.folder, args.test_y_path)

    model_name = args.model_name
    version = args.version
    num_classes = args.num_classes

    train_model(train_X_path,train_y_path,test_X_path,test_y_path)