'''
The following a python script takes in the inputs of the pi's camera.
Modified by Phillip Teng
9/18/2018

References:
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/5
'''

# import necessary libraries
from picamera import PiCamera
from time import sleep

# create instance of the camera
camera = PiCamera()
'''
# start preview (necessary)
camera.start_preview()

# delay for 10 seconds before closing preview.
sleep(10)
camera.stop_preview()

# now if we want to do something
'''

# downscale capture resolution
camera.resolution = (256, 144)

camera.start_preview()

# goes into a for loop five times and takes a picture once every 5 seconds and saves it.
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)

camera.stop_preview()

# we can then take the images and feed it into the car detection algorithm
