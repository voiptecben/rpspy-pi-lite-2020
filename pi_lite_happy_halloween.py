#!/usr/bin/env python

import serial
import time

# Define lists which contain frames of animations
face   = ['000000000000000000010011000011000100011000110000010110000110110000110110000010110011000110011000100010011000000000000000000000',
          '000000000000000000010000011011000110011000110000010110000110110000110110000010110011000110011000110010000011000000000000000000']
bat    = ['010000000011000000001100000000110000110110000011111011001111100001111100011111011110110000000110000001100000011000000010000000',
          '000000100000001100000011000000110000110110001011111010001111100001111100011111010110110001000110000000011000000001100000000100']        
ghost  = ['000000000000000000000011111001100001010000010100100010100000001100100001100000010010000010001100001000011111000000000000000000',
          '000000000000000000000011111001100010010000010100000001100100001100000010100100010010000001001100001000011111000000000000000000']
spider = ['001001000010010010100100101010101000001011110000111001000111000000111000000111001001011110010101000100100101010010010001001000',
          '010010010100100101101001000100101010011011101000111000000111000000111000000111000011011101100101010101001000100100101010010010']
   
# Combine    
objects = {'face':face,'bat':bat,'ghost':ghost,'spider':spider}
   
# Define text message to scroll
message = "Happy Halloween !\r"

# Configure Pi serial port
s = serial.Serial()
s.baudrate = 9600
s.timeout = 0
s.port = "/dev/ttyAMA0"

def showObject(name,count,delay):
  # Function to display frames from a specified object
  # name  - object to display
  # count - number of times to display object
  # delay - ms to wait between frames
  object = objects[name]
  for x in range(count):
    for frame in range(len(object)):
      command = "$$$F" + object[frame] + "\r"
      s.write(command)
      time.sleep(delay)
  # Clear display
  s.write("$$$ALL,OFF\r")    
  
try:
    # Open serial port
    s.open()
except serial.SerialException, e:
    sys.stderr.write("could not open port %r: %s\n" % (port, e))
    sys.exit(1)

# Turn off all LEDs
s.write("$$$ALL,OFF\r")
time.sleep(0.5)

while True:
  # Get list of object names
  mykeys = objects.keys()
  
  # Loop through each name
  for x in range(len(mykeys)):
    showObject(mykeys[x],5,0.5)
    time.sleep(1)     
    s.write(message)  
    time.sleep(8)  