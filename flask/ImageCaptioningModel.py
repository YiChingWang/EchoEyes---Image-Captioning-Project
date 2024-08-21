import torch
from PIL import Image
from torchvision.transforms import Compose, Resize, ToTensor, Normalize
from model import CNNtoRNN


class ImageCaptioningModel:
    def __init__(self, model_path, vocab, transform=None):
        self.vocab = vocab
        vocab_size = len(self.vocab)
        self.model = self.load_model(model_path, vocab_size)
        self.transform = transform or self.default_transform()

    def load_model(self, model_path, vocab_size):
        model = CNNtoRNN(embed_size=256, hidden_size=256,
                         vocab_size=vocab_size, num_layers=1)
        checkpoint = torch.load(model_path, map_location=torch.device('cpu'))
        model.load_state_dict(checkpoint['state_dict'])
        model.eval()
        return model

    def default_transform(self):
        return Compose([
            Resize((299, 299)),
            ToTensor(),
            Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def process_image(self, image_file):
        image = Image.open(image_file).convert('RGB')
        image = self.transform(image).unsqueeze(0)
        return image

    def generate_caption(self, image_tensor):
        with torch.no_grad():
            caption_indices = self.model.caption_image(
                image_tensor, self.vocab)

            caption_words = []
            for idx in caption_indices:
                if isinstance(idx, str):
                    idx = self.vocab.stoi[idx] if idx in self.vocab.stoi else '<unk>'

                if idx in [self.vocab.stoi['<SOS>'], self.vocab.stoi['<EOS>'], self.vocab.stoi['<UNK>']]:
                    continue

                word = self.vocab.itos[idx] if isinstance(
                    idx, int) and idx < len(self.vocab.itos) else '<unk>'
                caption_words.append(word)

            caption = ' '.join(caption_words)

            print("Generated caption:", caption)
            return caption
