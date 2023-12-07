# Professor If I used Python 3.9.13 for this code. I used the following libraries I am only telling you this because I moved it from my desktop to my laptop and I had to reinstall some of the libraries and ran into some issues with the versions of the libraries I was using:
import tensorflow as tf # This allows me to access functions, layers, and models to build and train neural networks.
from tensorflow.keras.preprocessing.image import ImageDataGenerator # This allows me to generate batches of tensor image data with real-time data augmentation.
from tensorflow.keras.models import Sequential # This allows me to build my neural network model layer by layer.
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout # These are the layers I am using to build my neural network.
from math import ceil # This allows me to round up numbers.

# I am using this to check if my 4070 GPU is available
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
print(tf.test.gpu_device_name())

# Set up ImageDataGenerators for training and validation it refrences the ART-COZMO folder where I stored the images
data_dir = "Cozmo-The-Art-Evaluator\ART-COZMO"

#I am using this to set up augmentations of my images in order to increase the accuracy of my model and the variablity
# of my images. It allows me to rotate, shift, zoom, and flip my images. I am also using it to rescale my images to a
# range of 0 to 1. The variation split allows me to monitor the accuracy of my model as it gets generated.
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
    validation_split=0.2
)

# This section sets up my training data. It tells the program to look in data_dir for images. It then changes 
# the size of each image to 224x224 pixels which is needed for my neural network to process them correctly
# and groups the images into batches each containing 32 images. This makes it easier to manage them
# during training. The class_mode being categorical means I’m trying to classify images into different 
# categories or classes. Finally subset is set to training means this setup is for training my model not 
# testing it.
batch_size = 32
train_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

# This sets up my validation data. It is similar to how I set up my training data but for validating the 
# model's performance. It still looks in data_dir for images then it resizes them to 224x224 pixels and groups them 
# into batches of 32 images each. Just like with the training data the images are used for a classification task.
# The key difference is subset is set to validation which means this setup is specifically for evaluating how well
# my model is learning rather than training it.
validation_generator = train_datagen.flow_from_directory(
    data_dir,   
    target_size=(224, 224), 
    batch_size=batch_size,  
    class_mode='categorical',  
    subset='validation' 
)

# Here I am calculating how many steps (or batches of images) my model needs to go through in one complete training 
# and validation cycle. train_steps_per_epoch is the total number of training images divided by the batch size 
# rounded up. This ensures my model sees all the training images in each training cycle. 
train_steps_per_epoch = ceil(train_generator.samples / batch_size)
validation_steps_per_epoch = ceil(validation_generator.samples / batch_size)

# This part of the code is where I build my neural network model layer by layer. It is like stacking building blocks:
# Conv2D layers are like camera lenses that look for patterns in the images. 
# relu activation helps the model understand these patterns better.
# MaxPooling2D layers (2x2) reduces the image size while keeping the important features making processing faster.
# After the Conv2D and MaxPooling layers the Flatten layer turns the 2D features into a 1D format like 
# unrolling a sheet of paper so it can be processed by the next layers. A Dense layer with 512 neurons takes
# all the patterns learned and starts making sense of them.
# The final Dense layer has 7 neurons because I have 7 different artworks and softmax activation gives 
# me a probability-like output for each artwork category telling me how likely the image belongs to each category.

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(7, activation='softmax')
])

# Here I am setting up how the model learns. I use adam as the optimizer which is a way to change the model to 
# improve its predictions. The loss is how the model measures its mistakes using categorical_crossentropy 
# because I am classifying images into categories. I am tracking accuracy to see how often the model's 
# predictions are correct.
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Now I am training the model with my images. It uses the training data train_generator and validation data 
# validation_generator for 20 rounds epochs. steps_per_epoch tells it how many batches of images to use 
# per epoch for training and validation_steps does the same for validation. This way the model learns from 
# the training data and checks how well it's doing with the validation data.
history = model.fit(
    train_generator,
    steps_per_epoch=train_steps_per_epoch,
    epochs=20,
    validation_data=validation_generator,
    validation_steps=validation_steps_per_epoch
)

# Save the trained model
model.save('Art_Eval_For_Cozmo_The_Evaluator_2.keras')
