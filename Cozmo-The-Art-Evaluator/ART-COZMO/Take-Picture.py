# Professor If I used Python 3.9.13 for this code. I used the following libraries I am only telling you this because I moved it from my desktop to my laptop and I had to reinstall some of the libraries and ran into some issues with the versions of the libraries I was using:
import time # I am using this for timing my program.
import cozmo # just cozmo related stuff. I am using this to make Cozmo talk and move.
import asyncio # I am using this to make Cozmo wait for user input.
from cozmo.util import degrees # I am using this to make Cozmo move his head.
from cozmo.objects import LightCube1Id # I am using this to make Cozmo react to the cubes.

# I am setting the initial head angle (in degrees).
initial_head_angle = 22

def capture_and_save_image(robot, image_count):
    # Set the head angle.
    robot.set_head_angle(degrees(initial_head_angle)).wait_for_completed()
    
    # Take a picture and save with a unique name.
    image = robot.world.latest_image.raw_image
    image.save(f"Johanne Vermeer The Girl With a Pearl Earring 1632{image_count}.png", 'PNG') #this was my last saved name but it can be changed to whatever is needed.

    # This starts my color stream for the camera.
def cozmo_program(robot: cozmo.robot.Robot):
    image_count = 0
    robot.camera.image_stream_enabled = True
    robot.camera.color_image_enabled = True

    # Connect to the light cube and turn it green if connected successfully.
    robot.world.connect_to_cubes()
    cube1 = robot.world.get_light_cube(LightCube1Id)
    if cube1:
        cube1.set_lights(cozmo.lights.green_light)
    else:
        cozmo.logger.warning("Lightcube for Cozmo is not connected maybe the battery is dead.")

    # Function to handle cube taps for cube 1.
    def on_cube_tap1(evt, **kwargs):
        nonlocal image_count
        image_count += 1
        asyncio.ensure_future(capture_and_save_image(robot, image_count))

    # This is the event handler for cube 1.
    cube1.add_event_handler(cozmo.objects.EvtObjectTapped, on_cube_tap1)

    # Keep the program running until stopped by user.
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("The program has stopped.")

# Run the program with the camera viewer on top.
cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)
