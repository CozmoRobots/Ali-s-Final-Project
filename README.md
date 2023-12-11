# Ali-s-Final-Project
Cozmo the Art Evaluator

Setup Instructions
First, install Python version 3.9.13. This was the version used to create the code, using the same version will reduce the number of potential errors (when the code was written any version above 3.9.13 gave me errors). Next, run the requirements.txt file that is in the Ali-s-Final-Project GitHub to set up an environment with all the necessary dependencies. You can install all the listed requirements by running 
pip install -r Cozmo-The-Art-Evaluator/requirements.txt
in the terminal in the project folder.
After that if you do not have my model, you can generate your own by running 
Art-Recognition-Model.py
and it will train the model using the approximately six thousand photos that were taken using Cozmo and uploaded to the Ali-s-Final-Project GitHub. The IDE used to create and run this program was VS Code, select the file and then hit the run dropdown and select “run without debugging”. The runtime for training was about twenty-five minutes. I am using a NVidia 4070 GPU and a Ryzen 7800x3d CPU, so my training was quick.
	Next you can plug your iOS device into your computer (make sure that iTunes is running in the background on the computer). Then connect your iOS device to Cozmo via direct Wi-Fi connection. Then run the Cozmo app and Cozmo should come to life and start. Then launch SDK mode in the app. From there you will run
Cozmo-The-Art-Evaluator.py
if you generated your own model you will need to change line 13 in the Cozmo-The-Art-Evaluator.py file from
model = tf.keras.models.load_model('Cozmo-The-Art-Evaluator\ART-COZMO\Art_Eval_For_Cozmo_The_Evaluator.keras')
to
model = tf.keras.models.load_model('your model path here’)
your Cozmo robot will then begin giving instructions on how to use the cubes for interacting with Cozmo the art evaluator, during the art appraisal process. Cozmo will then appraise the art hopefully deducing the proper art piece. Since the program is set up to be an endless loop, if you want to stop Cozmo, you can terminate the run (in VS Code you would hit the Stop Button in the run overlay).
