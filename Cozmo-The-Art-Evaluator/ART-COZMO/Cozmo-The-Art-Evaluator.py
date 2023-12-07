# Professor If I used Python 3.9.13 for this code. I used the following libraries I am only telling you this because I moved it from my desktop to my laptop and I had to reinstall some of the libraries and ran into some issues with the versions of the libraries I was using:
import time # I am using this for timing my program.
import cozmo # just cozmo related stuff. I am using this to make Cozmo talk and move.
import asyncio # I am using this to make Cozmo wait for user input.
from cozmo.util import degrees # I am using this to make Cozmo move his head.
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id # I am using this to make Cozmo react to the cubes.
from PIL import Image # I am using this to process the images that Cozmo sees.
import numpy as np # I am also using this to process the images that Cozmo sees.
import tensorflow as tf # I am using this to load my model and make predictions.


# I am loading the model that I trained in Art-Recognition-Model.py. I am using this to predict the art that Cozmo sees.
model = tf.keras.models.load_model('Cozmo-The-Art-Evaluator\ART-COZMO\Art_Eval_For_Cozmo_The_Evaluator.keras')

# List of Art I am using for my model. I am using a variety of art styles and types: 
# AI art mountain lake trees.
# AI art street lights and trees.
# Edvard Munch The Scream 1893.
# Georges Seurat A Sunday Afternoon on the Island of La Grande Jatte 1884–1886.
# Georgia O’Keeffe Red Canna 1924.
# Johanne Vermeer The Girl With a Pearl Earring 1632-1675.
# René Magritte The Son of Man 1964.

# Art Information Database
# I am storing all of the Phrases that I want to use in a dictionary. I am using this to make it easier to call them later.
art_database = {
    "Edvard-Munch-The-Scream-1893": {
        "name": " This is The Scream.",
        "remark": "This is a very famous painting and I think it will sell for a lot of money.",
        "artist": "The artist is Edvard Munch.",
        "year": "It was painted in Eighteen ninety three.",
        "style": "The style is Expressionism.",
        "description": "This is one of Munch's four versions of 'The Scream', it symbolizes modern existential angst and has an iconic status in art history.",
        "appraisal": "I want to offer you one hundred and fifty million dollars how does that sound?"
    },
    "Georges-Seurat-A-Sunday-Afternoon": {
        "name": " This is A Sunday Afternoon on the Island of La Grande Jatte.",
        "remark": "This is a very famous painting and I think it will sell for a ton of money.",
        "artist": "The artist is Georges Seurat.",
        "year": "It was painted in eighteen eighty five.",
        "style": "The style is Post-Impressionism, Pointillism.",
        "description": "This is a masterpiece of pointillism, capturing the leisurely activities of Parisians at La Grande Jatte island on the Seine River. I love the colors that are used in this one",
        "appraisal": "I am excited to offer you one hundred million dollars does that sound good to you?"
    },
    "Georgia-OKeeffe-Red-Canna-1924": {
        "name": " This peice is Red Canna.",
        "remark": "This is a very famous painting and I think it will sell for a good chunk of change.",
        "artist": "The artist is Georgia O'Keeffe.",
        "year": "It was painted in Nineteen twenty four.",
        "style": "The style is American Modernism.",
        "description": "This is part of O'Keeffe's famous series of flower paintings, Red Canna is celebrated for its vibrant colors and bold depiction.",
        "appraisal": "I would like to make an offer for forty five millions dollars and fifty cents don't think about it too much just say yes."
    },
    "Pearl-Earring": {
        "name": "This artwork is The Girl With a Pearl Earrings.",
        "remark": "This is a very famous painting and I think it will sell for way too much money.",
        "artist": " The creator of this art is Johannes Vermeer.",
        "year": "It was created in sixteen sixty five.",
        "style": "The style is Dutch Golden Age.",
        "description": " This painting is ofter referred to as the Mona Lisa of the North, this painting is renowned for its exquisite detail and emotional depth. I really love the way that she looks of to the side.",
        "appraisal": "How dows one hundred and twenty million dollars sound lets make a deal?"
    },
    "Mountain-AI-Lake-Training-Photos": {
        "name": " I am not sure what the name is but it seems very serene.",
        "remark": "I am not sure that this will sell for very much. It would look nice in a waiting room though.",
        "artist": "I do not recognize the artist.",
        "year": "I am not sure when this was made.",
        "style": "The style seems to be A I Generated Art.",
        "description": "What a nice serene depiction of a mountain and a lake surrounded by trees, it is kind of crazy what A I is capable of in art creation.",
        "appraisal": "Best I can offer is thirty dollars and sixty three cents."
    },
    "René-Magritte-The-Son-of-Man-1964": {
        "name": "This is beautiful art peice is The Son Of Man.",
        "remark": "This is a very impressive piece of art and I think it will sell for a lot more than you think.",
        "artist": "The artist who painted this is René Magritte.",
        "year": "It was created in Nineteen sixty four.",
        "style": "The style is Surrealism",
        "description": "The painting is a self-portrait with a twist, The Son of Man skillfully plays with reality and perception, featuring a man's face obscured by a floating apple. I think it is pretty cool how the apple is covering his face.  He also has a nice suit on.",
        "appraisal": "I know that some of the other painting are worth more but I am only willing to offer twenty seven million dollars based on how much I think I can sell it for."
    },
        "Street-Lights-And-Trees-AI-Art": {
        "name": " I am not sure what the name is but it is pretty.",
        "remark": " I am not sure that this will sell for very much. But it would make a nice accent piece in a living room.",
        "artist": "I am not familiar with the artist.",
        "year": "I honestly do not know.",
        "style": "The style seems to be AI-Generated Art.",
        "description": "I believe that this is an AI-generated artwork featuring street lights illuminating a path lined with trees, reflecting a quiet urban scene. It is quite pretty but not very authentic.",
        "appraisal":  "All I can offer is fifty dollars."
    }
}

# This is my dictionary class_indices it lets me maps numbers to the names of artworks. Each number represents a specific 
# artwork category. This helps my model understand which number corresponds to which artwork when it makes predictions.
class_indices = {
    0: "Edvard-Munch-The-Scream-1893",
    1: "Georges-Seurat-A-Sunday-Afternoon",
    2: "Georgia-OKeeffe-Red-Canna-1924",
    3: "Pearl-Earring",
    4: "Mountain-AI-Lake-Training-Photos",
    5: "René-Magritte-The-Son-of-Man-1964",
    6: "Street-Lights-And-Trees-AI-Art",    
}

# The function I wrote below takes an image and prepares it for analysis by the AI model. First it changes the 
# size of the image to 224x224 pixels because that is the size my model expects. Then it converts the image into 
# a numpy array so that my model can understand its colors and processes them correctly. 
# After that the model tries to predict what artwork that the image is and I translate this prediction 
# into the name of the artwork using my function above.
def process_image(image):
    processed_image = image.resize((224, 224))
    processed_image = np.array(processed_image) / 255.0
    processed_image = np.expand_dims(processed_image, axis=0)
    predictions = model.predict(processed_image)
    predicted_index = np.argmax(predictions)    
    predicted_art_name = class_indices[predicted_index]
    return predicted_art_name

# I wrote this function to fetche details about an artwork from art_database using its name. 
# If the artwork name is not found, it returns default_info, which includes placeholders like Unknown for 
# various details (name, artist, year, etc.). This ensures that the program always has some information to provide, 
# even if the specific artwork is not recognized.
def get_art_info(art_name):
    default_info = {
        'name': 'Unknown',
        'remark': 'No information available.',
        'artist': 'Unknown',
        'year': 'Unknown',
        'style': 'Unknown',
        'description': 'No description available.',
        'appraisal': 'No appraisal value available.'
    }
    return art_database.get(art_name, default_info)

# In this function I am telling Cozmo to capture and process an image. First I adjust Cozmo's head angle to 22 degrees 
# to get a good view of the artwork. After Cozmo looks up I grab the latest image that Cozmo sees. Then I use the 
# process_image function I wrote earlier to figure out what artwork is in the image. This function gives me back the 
# name of the artwork which I then return from this function.
async def capture_and_process_image(robot):
    await robot.set_head_angle(degrees(22)).wait_for_completed()
    image = robot.world.latest_image.raw_image
    art_name = process_image(image)
    return art_name

# This function lets Cozmo react when someone taps the Yes or No cubes. It waits until a cube is tapped and 
# then makes Cozmo say a different phrase depending on which cube was tapped, with a bit of a faster speech.
# I am doing this to let the user know that Cozmo is listening to them and that he is reacting to their input.
async def handle_user_response(robot, yes_cube, no_cube):
    yes_tapped = False
    no_tapped = False
    
    # I am using these functions to tell Cozmo to react when the yes cube is tapped.
    def on_yes_cube_tap(evt, **kwargs):
        nonlocal yes_tapped
        yes_tapped = True
    
    # I am using these functions to tell Cozmo to react when the no cube is tapped.
    def on_no_cube_tap(evt, **kwargs):
        nonlocal no_tapped
        no_tapped = True
        
    # I am using these functions to tell Cozmo to react when the yes cube is tapped.
    yes_cube.add_event_handler(cozmo.objects.EvtObjectTapped, on_yes_cube_tap)
    no_cube.add_event_handler(cozmo.objects.EvtObjectTapped, on_no_cube_tap)

    # This will wait until one of the cubes is tapped.
    while not (yes_tapped or no_tapped):
        await asyncio.sleep(0.1)
        
    # Here are the phrases that Cozmo says when the user taps the Yes or No cubes I wanted to make him seem professional.
    if yes_tapped:
        await robot.say_text("It has been a pleasure doing business you!", duration_scalar=0.65).wait_for_completed()
    elif no_tapped:
        await robot.say_text("Your loss, I've got the best offers around!", duration_scalar=0.65).wait_for_completed()

# In this part of my code I am setting up the main program for Cozmo. First I turn on Cozmo's camera so it can stream 
# images and make sure it captures color images. Then I make sure Cozmo can connect to the interactive cubes which 
# are part of how I will interact with Cozmo during the art appraisal.

def cozmo_program(robot: cozmo.robot.Robot):
    robot.camera.image_stream_enabled = True
    robot.camera.color_image_enabled = True
    robot.world.connect_to_cubes()

    # I am setting up my cubes below. I am using the light cubes as user inpurt for making decisions during the appraisal.
    yes_cube = robot.world.get_light_cube(LightCube2Id)  # Cube for Yes response.
    no_cube = robot.world.get_light_cube(LightCube3Id)   # Cube for No response.
    camera_cube = robot.world.get_light_cube(LightCube1Id)  # Cube to start camera.

    # I am setting the light colors for cubes below I want blue for capture cube, green for yes cube, and red for no cube.
    # I also have a warning message that will display if a cube is not connected. This is to let me know if I need to
    # check my connections if they are not working.
    if yes_cube is not None:
        yes_cube.set_lights(cozmo.lights.green_light)
    else:
        cozmo.logger.warning("Yes Cube (LightCube2) is not connected maybe the battery is dead.")

    if no_cube is not None:
        no_cube.set_lights(cozmo.lights.red_light)
    else:
        cozmo.logger.warning("No Cube (LightCube3) is not connected maybe the battery is dead.")

    if camera_cube is not None:
        camera_cube.set_lights(cozmo.lights.blue_light)
    else:
        cozmo.logger.warning("Camera Cube (LightCube1) is not connected maybe the battery is dead.")

    # When I or the appriasee tap the camera cube I have set up Cozmo to start the art appraisal process. Cozmo tells us to hit the Blue cube to begin. 
    # Cozmo then captures an image and tries to identify the artwork. I added a print statement to see which artwork Cozmo thinks it is.
    # Cozmo talks about the artwork, like its name, remark, artist, year, style, description, and what it might be worth while speaking a bit quicker than usual.
    # Finally Cozmo asks for a response by hitting the Green cube to agree or the Red cube to disagree with the offer and I handle this response in another function
    # that I wrote above.
    async def on_camera_cube_tap(evt, **kwargs):

        # I am using this to explain the user input process to the user.        
        await robot.say_text(f"Hit the Blue cube to start the appraisal process.", duration_scalar=0.65).wait_for_completed()
        
        # This is the prediction part of my program. I am using this to tell Cozmo to capture and process an image.
        art_name = await capture_and_process_image(robot)
        print("Predicted Art Name:", art_name)
        art_info = get_art_info(art_name)
        
        # I am using this to tell Cozmo to talk about the artwork that he sees.        
        await robot.say_text(f"{art_info['name']}", duration_scalar=0.65).wait_for_completed()
        await robot.say_text(f"{art_info['remark']}", duration_scalar=0.65).wait_for_completed()
        await robot.say_text(f"{art_info['artist']}", duration_scalar=0.65).wait_for_completed()
        await robot.say_text(f"{art_info['year']}", duration_scalar=0.65).wait_for_completed()
        await robot.say_text(f"{art_info['style']}", duration_scalar=0.65).wait_for_completed()
        await robot.say_text(f"{art_info['description']}", duration_scalar=0.65).wait_for_completed()
        await robot.say_text(f"{art_info['appraisal']}", duration_scalar=0.65).wait_for_completed()
        
        # I am using this to explain the user input process to the user for accepting or declining the offer.
        await robot.say_text(f"Hit the Green cube if you want to accept the offer other wise you can hit the red cube to decline my generous offer.", duration_scalar=0.65).wait_for_completed()
        
        # I am using this to make Cozmo wait for user input.
        await handle_user_response(robot, yes_cube, no_cube)

    # I am using this to tell Cozmo to start the appraisal process when the camera cube is tapped.
    camera_cube.add_event_handler(cozmo.objects.EvtObjectTapped, on_camera_cube_tap)
    
    # I am using this while loop to keep my program running. I am using a try and except statement to catch any errors that might occur.
    while True:
        time.sleep(1)

# This is where I am running my program. I am using the force_viewer_on_top=True to make sure that the viewer window is always on top.
cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)
