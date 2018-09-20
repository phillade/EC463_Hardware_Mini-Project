# Senior Design Hardware Mini Project
#### By Phillip Teng and Howard Han
#### 9/20/2018

## Introduction: 
The following project is to demonstrate a simple attempt at counting the number of cars and bicycles on the road using a Raspberry Pi Zero W and a high definition camera module. We will look at the results and provide preliminary results to showcase the dependence of the OpenCV algorithm on resolution. 

Design Methodology:
	The hardware component is relatively simple. We have a raspberry pi zero and a camera module that feed the video into a python script. Afterwards, the video is processed in python using the OpenCV wrapper library. This library provides the XML files for both car and bicycle detection.
	The software component of the project was developed in three different stages. The first stage was developing the software on laptops because they are much more powerful than the Pi. This allowed us to rapidly iterate through software versions without having the relatively large computation times on the Pi. The second stage was prototyping on a Raspberry Pi 2 B. The processor is a bit more powerful than than the Pi Zero that we were provided. The thinking was so that we could slowly optimize the code as we went along in the software development process later on as our hardware requirements are shrunk. The Pi 2 B has a four core Broadcom CPU running at 900 MHz instead of a single one at 1 GHz for the Pi Zero W. The final stage of software development was to run it on the Pi Zero.
	Our software component features a couple features including 

< Insert Pictures showing Raspberry Pi >
![Setup](https://i.imgur.com/ve2Jf4d.jpg)

Figure 1: Showing the setup for the Pi 2 B.
![Car detection algorithm](https://i.imgur.com/aF1naWq.png)
Figure 2: Showing the sample output of the video feed in car detection.
![SSHing into Pi](https://i.imgur.com/wfaSH5f.png)
Figure 3: Showing sucessful SSH across the internet after determining the Pi IP address with "hostname -I".

## Process:
The first thing we did was to install raspbian desktop version onto Pi Zero. After finagling with getting the internet to work, we installed all the required packages as detailed below. The process of getting SSH to work can be found in the second link under the section “References”. We used SCP to copy manage the transfer of files between our laptops and the Pi.

## Testing Methodology:
For the software component, we decided to utilize the existing code library known as OpenCV. We realized that the simplest way would be to take in existing code from the internet and repurpose it to take in a video stream from the webcam. Due to the limitations of the processor on the Pi Zero, we decided to take a lower resolution picture once every second and then use that to count the number of cars. At HD quality, the Pi takes more than 5 seconds to process one frame. As such, we had to lower the resolution collected from the camera down to 480. It’s still very slow, roughly taking 2 seconds per frame.
The software library we used was provided and installed on Raspbian Stretch Desktop version. We included the Picamera library module along with numpy and cv2. 

## Results:
![Resolution dependence](https://i.imgur.com/tlrTZAO.png)
Figure 3: This chart shows the dependence the car counting algorithm on the resolution of the video in reference to the number of actual cars on the road. The real number of cars was counted by humans.
![What is going on]()
Figure 4: This chart shows the dependence of the bike counting algorithm and its impact on bikes.

## Discussion:

As seen in Figure 1, our system actually performs relatively well. The number of false detections and false negative is relatively low. False detection definitely exists, but as seen in our testing, the box usually goes around the car lights, but does not over count the number of cars. The error of false detection is also much smaller than the error of not detecting cars that are far away and therefore are presented to the computer as black or white boxes. This theory also supports what we see in Figure 1 because part of the reason the car detection algorithm under estimates the number of cars is that the cars would get too small for the algorithm to tell that the box is a car, whereas a human can.


Future work and potential improvements:
	The limiting factor in this system is definitely the hardware. The Pi Zero used in this project is simply not powerful enough for real time car detection. The algorithm that uses the XML file generated from OpenCV is simply too computationally intensive. As the results showed, there is a huge trade off in getting accurate car detection when limited by resolution. The accuracy of the system is definitely improved with a higher definition camera, but in turn a much more powerful CPU to complement it. This solution would therefore be more expensive to implement, but it would be much more useful.

We chose OpenCV mainly because of our past experiences using such a powerful library. However we were also able to show that the accuracy of the system to almost model the real number of cars. The same could be applied to bicycles. Our software also implements 

Another creative way that we could improve accuracy is to use the sound component of a video. Add a microphone and we would be able to predict whether or not cars are approaching and it could be included in the model and the model would have an additional metric to decide whether or not the sound is “car sounding”. Using motion tracking sensor could also be used as an additional metric. But both solutions will require more computational power.

Part of future works we can do is to try other test cases. Much of the software development occurred with a front on view instead of a side on view of the cars and bicycle. The algorithm may or may not work better from the side, more testing is needed to reveal that.


## Appendix:

### References used:
https://github.com/phillade/EC463_Mini-Project/
https://desertbot.io/blog/headless-pi-zero-ssh-access-over-usb-windows
https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
http://ask.xmodulo.com/disable-desktop-gui-raspberry-pi.html
https://github.com/BostonUniversitySeniorDesign/hardware-project-2018/wiki


### Python Packages installed:
Pip <br/>
Numpy <br/>
Matplotlib <br/>
Opencv-python <br/>

### Hardware utilized:
Pi Zero W - The CPU serial number is 00000000acb920d9 <br/>
Pi 2 B <br/>
Pi Camera <br/>
Micro-USB cable <br/>
Keyboard <br/>
Mouse <br/>
Monitor <br/>

