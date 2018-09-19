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
import numpy as np

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
    camera.capture('/home/pi/Desktop/image%03s.jpg' % i)

cap = cv2.VideoCapture('cars_%03d.jpg4')

camera.stop_preview()

# we can then take the images and feed it into the car detection algorithm


#create VideoCapture object and read from video file
#cap = cv2.VideoCapture('cars.mp4')
cap = cv2.VideoCapture('cars_%03d.jpg')
#cap = cv2.VideoCapture('cars_480.mp4')
#cap = cv2.VideoCapture('cars_360.mp4')

#write video out
#out = cv2.VideoWriter('output.mp4', -1, 20.0, (640,480))

#use trained cars XML classifiers
car_cascade = cv2.CascadeClassifier('cars.xml')

file = open('output.txt', 'w')

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
    file.write("{}\n".format(car_count))

    #press q on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

#release the videocapture object
cap.release()
#out.release()
#close all the frames
cv2.destroyAllWindows()
file.close()
