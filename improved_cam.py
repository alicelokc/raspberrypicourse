# import libraries
import picamera
import time
import datetime
import imageio
import glob
import os

# Initialise the camera
camera = picamera.PiCamera()

# Camera set up
camera.resolution = (1280, 720)
camera.framerate = 30

#wait for the automatic gain control to settle
time.sleep(2)

# Now fix the value
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

# Take the photo and store in the images folder, with the filename of a unxi timestamp
#camera.capture('/home/pi/raspberrypicourse/time-lapse/%s.jpg' % (datetime.datetime.now()))
camera.capture('./time-lapse/%s.jpg' % (datetime.datetime.now()))

with imageio.get_writer('./time-lapse/animate.gif', mode ='I') as writer:
    filenames = glob.glob("./time-lapse/*.jpg")
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

os.system("sudo cp ./time-lapse/animate.gif /var/www/html")
        

