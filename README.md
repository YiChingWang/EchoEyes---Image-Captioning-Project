# EchoEyes

## Introduction

EchoEyes is an innovative web-based application designed to assist visually impaired individuals in interpreting their environment. By leveraging advanced image captioning and Text-to-Speech (TTS) technology, EchoEyes provides a robust and user-friendly interface. The application is developed using Python with Flask as the backend framework and managed using Visual Studio Code.

## Technology Overview

### Image Captioning

EchoEyes employs advanced neural networks for image captioning, involving the following processes:

- **Feature Extraction:** Utilizes Convolutional Neural Networks (CNNs) to analyze images and extract features.
- **Caption Generation:** Employs Recurrent Neural Networks (RNNs) or Long Short-Term Memory (LSTM) networks to generate coherent captions based on the extracted features.

### Text-to-Speech (TTS)

EchoEyes integrates a TTS API that converts written text into spoken words, enhancing accessibility for visually impaired users.

### Video Overview

Watch the EchoEyes Demo Video

![EchoEyes Demo](https://i.imgur.com/nytLJWo.gif)

## Setup Instructions

### Prerequisites

1. **Download Flick8r**: [https://www.kaggle.com/datasets/adityajn105/flickr8k](#)
2. **Download TAR File**: [https://drive.google.com/drive/folders/1NFYLXv09IlGnnsaaV6-\_rIZINqQzVOKk?usp=sharing](#)

### Configuration

After downloading the Flick8r dataset and TAR file, you need to update the paths in your code to ensure everything runs smoothly.

1. **Update Flick8r Path:**

   Modify the following files to reflect the correct path to the Flick8r dataset:

   - `app.py`
   - `getloader.py`
   - `runCaption.py`

   For example:

   ```python
   flickr8k_path = "/Users/olliesmacbook/Desktop/echoeyes pyhton  final project/EchoEyes/flask/flickr8k/Images", "/Users/olliesmacbook/Desktop/echoeyes pyhton final project/EchoEyes/flask/flickr8k/captions.txt", # Update this path
   ```

2. **Update TAR File Path:**

   Similarly, update the path to the TAR file in the following
   files:

   - `utils.py`
   - `app.py`
   - `runCaption.py`

   For example:

   ```python
   model_path = "/Users/olliesmacbook/Desktop/echoeyes pyhton     final project/EchoEyes/my_checkpoint.pth_backup.tar"  # Update this path
   ```

### Virtual Environment Setup

To ensure that your environment is correctly set up with all the necessary dependencies, follow these steps to create and activate a virtual environment:

**Create a Virtual Environment**

First, navigate to the project directory and create a virtual environment:

```bash
python -m venv env
```

This command will create a new virtual environment in a folder named env.

**Activate the Virtual Environment**

On Windows:

```bash
.\env\Scripts\activate
```

On macOS and Linux:

```bash
source env/bin/activate
```

Once the virtual environment is activated, your terminal prompt will change to reflect that you're working inside the virtual environment.

**Install Dependencies**

After activating the virtual environment, install the required dependencies from the requirements.txt file:

```bash
pip install -r requirements.txt
```

This will install all the necessary packages needed to run the application.

**Deactivating the Virtual Environment**
When you're done working on the project, you can deactivate the virtual environment by running:

```bash
deactivate
```

This will return your terminal to the global Python environment.

### Installation

1. **Clone the Repository**

   ```bash
   git clone git@github.com:YiChingWang/EchoEyes----Image-Captioning-Project.git
   ```

2. **Set Up the API**
   Obtain API keys for image captioning and TTS services.
   Configure the API keys in the config.py file or environment
   variables as specified in the documentation.

### Running the Application

1. **Start the Flask Server**
   ```bash
   python app.py
   ```
2. **Access the Web Application**
   Open your web browser and navigate to:

   ```bash
   http://localhost:5020
   ```

### API Usage

For detailed information on API usage, refer to the API Documentation provided in the repository.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
