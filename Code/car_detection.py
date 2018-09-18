'''
This script utilizes OpenCV to count the number of cars given jpg or mp4 files.

It then saves the output for comparison.
Modified by Phillip Teng
9/18/2018

References:
https://www.youtube.com/watch?v=IM9hJte4DZY&t=2s
https://stackoverflow.com/questions/29317262/opencv-video-saving-in-python

'''

#import libraries of python opencv
import cv2
import numpy as np

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