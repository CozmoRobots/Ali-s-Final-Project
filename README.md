# Ali-s-Final-Project
Cozmo the Art Evaluator

README for Cozmo-The-Art-Evaluator.py
Overview
"Cozmo-The-Art-Evaluator.py" is a Python script I wrote for integrating a trained art recognition model with Cozmo, a small robot by Anki. It allows Cozmo to recognize artworks and interact with users based on their responses.

Key Features
Cozmo Integration: The script enables Cozmo to use its camera to capture images and then recognize the artworks using the pre-trained model.
User Interaction: Cozmo interacts with users through voice and light cubes, responding to their inputs during the art appraisal process.
Art Database: The script references an art database containing information about various artworks, which Cozmo uses to provide details on recognized art pieces.
Functionality
Art Recognition: Cozmo captures images and identifies artworks using the "process_image" function.
Speech Output: Cozmo provides information about the artwork and its appraisal value, speaking a bit faster for a smoother interaction.
User Response Handling: The script allows Cozmo to wait for and react to user inputs using the light cubes.
Running the Program
The script is run using Cozmo's SDK, with the viewer window always on top for real-time interaction feedback.

README for Art-Recognition-Model.py
Overview
"Art-Recognition-Model.py" is a Python script I created for training an AI model to recognize different artworks. I used Python 3.9.13 and TensorFlow for this project.

Key Features
Model Training: The script uses TensorFlow to build and train a Convolutional Neural Network (CNN) model.
Image Data Augmentation: I implemented image augmentation techniques to increase the model's accuracy and variability in recognizing artworks.
GPU Utilization Check: The script checks for the availability of a GPU, which is crucial for efficient training.
ImageDataGenerator: I used this to automatically process and augment images from a specified directory.
Model Architecture
The model consists of several convolutional and pooling layers, followed by dense layers. The final output layer has 7 neurons, corresponding to 7 different artworks.