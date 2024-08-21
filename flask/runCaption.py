from torchvision.transforms import Compose, Resize, ToTensor, Normalize
from getloader import get_loader
from ImageCaptioningModel import ImageCaptioningModel

transform = Compose([
    Resize((224, 224)), 
    ToTensor(), 
    Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

train_loader, dataset = get_loader(
    root_folder="/Users/olliesmacbook/Desktop/Project/Echoeyes -- image captioning project/EchoEyes/EchoEyes----Image-Captioning-Project/flask/flickr8k/Images",
    annotation_file="/Users/olliesmacbook/Desktop/Project/Echoeyes -- image captioning project/EchoEyes/EchoEyes----Image-Captioning-Project/flask/flickr8k/captions.txt",
    transform=transform, 
    num_workers=2,
)

vocab = dataset.vocab
print("Is itos in vocab:", hasattr(vocab, 'itos'))

model_path = '/Users/olliesmacbook/Desktop/Project/Echoeyes -- image captioning project/EchoEyes/EchoEyes----Image-Captioning-Project/my_checkpoint.pth_backup.tar'
image_captioning_model = ImageCaptioningModel(model_path, vocab)

image_file = '/Users/olliesmacbook/Desktop/Project/Echoeyes -- image captioning project/EchoEyes/EchoEyes----Image-Captioning-Project/flask/flickr8k/Images/69189650_6687da7280.jpg'
image_tensor = image_captioning_model.process_image(image_file)
caption = image_captioning_model.generate_caption(image_tensor)
