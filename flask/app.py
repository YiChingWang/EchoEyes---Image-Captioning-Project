from ImageCaptioningModel import ImageCaptioningModel
from getloader import get_loader
import torchvision.transforms as transforms
from google.cloud import texttospeech
from flask import Flask, jsonify, render_template, request, url_for
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/olliesmacbook/Desktop/Project/Echoeyes -- image captioning project/birdy-405203-02c6cb586696.json"

app = Flask(__name__)

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])
loader, dataset = get_loader(
    "/Users/olliesmacbook/Desktop/Project/Echoeyes -- image captioning project/EchoEyes/EchoEyes----Image-Captioning-Project/flask/flickr8k/Images",
    "/Users/olliesmacbook/Desktop/Project/Echoeyes -- image captioning project/EchoEyes/EchoEyes----Image-Captioning-Project/flask/flickr8k/captions.txt",
    transform=transform
)

vocab = dataset.vocab

model_path = "/Users/olliesmacbook/Desktop/Project/Echoeyes -- image captioning project/EchoEyes/EchoEyes----Image-Captioning-Project/my_checkpoint.pth_backup.tar"
image_captioning_model = ImageCaptioningModel(model_path, vocab)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate_caption', methods=['POST'])
def generate_caption():
    try:
        file = request.files['image']
        if not file:
            return jsonify({'error': 'No file uploaded'}), 400

        image_tensor = image_captioning_model.process_image(file)
        print("Image Tensor:", image_tensor)

        caption = image_captioning_model.generate_caption(image_tensor)
        print("Generated Caption:", caption) 

        audio_content = text_to_speech(caption)
        print("Audio Content Length:", len(audio_content)) 

        audio_file_path = "flask/static/caption_audio.mp3"
        with open(audio_file_path, "wb") as out:
            out.write(audio_content)

        import os
        if os.path.exists(audio_file_path):
            print("Audio file created successfully.")
        else:
            print("Failed to create audio file.")

        return jsonify({'caption': caption, 'audio_path': url_for('static', filename='caption_audio.mp3')})

    except Exception as e:
        print(f"Error: {e}") 
        return jsonify({'error': str(e)}), 500

# tts
client = texttospeech.TextToSpeechClient()

def text_to_speech(text):
    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    return response.audio_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5020, debug=False) 
