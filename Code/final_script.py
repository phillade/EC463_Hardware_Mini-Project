'''
The following script takes in the camera input and then does car recognition on the image.
Modified by Phillip Teng
9/18/2018

References:
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/5
'''

# import necessary libraries
from picamera import PiCamera
from time import sleep
import cv2
import subprocess
import h5py


## function defines
# create instance of the camera
camera = PiCamera()

# downscale capture resolution
camera.resolution = (640, 480)

# record 10 seconds of video
camera.start_preview()
camera.start_recording('/home/pi/Desktop/Code/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()

# Run bash script to change video.h264 to video.mp4
rc = subprocess.call('MP4Box -fps 30 -add video.h264 video.mp4', shell=True)
if rc != 0:
    print "bash script failed to run"

# Load video into cv2
cap = cv2.VideoCapture('video.mp4')

# get car xml
car_cascade = cv2.CascadeClassifier('cars.xml')

#read until video is completed
while True:
    #reset car count to 0 for each frame
    car_count = 0

    #capture frame by frame
    ret, frame = cap.read()

    #convert video into gray scale of each frames
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        pass
    except cv2.error:
        break

    #detect cars in the video
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)

    #to draw arectangle in each cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        car_count = car_count + 1

    #display the resulting frame
    cv2.imshow('video', frame)

    #out.write(frame) # writes to output file
    print "{}".format(car_count)
    with h5py.File('mydat.h5', 'w') as f:
        f['dat'] = car_count

#release the videocapture object
cap.release()

#close all the frames
cv2.destroyAllWindows()
