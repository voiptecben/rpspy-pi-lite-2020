#!/usr/bin/env python
#--------------------------------------
#
# Pi-Lite Custom Example #2
#
# Author : Matt Hawkins
# Date   : 05/10/2013
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

import serial
import time

# Define message complete with
# carriage return at the end

paddlock = ['000000000000000000000000000000011111011111111111111111110011111110011111111111111011111111000011111000000000000000000000000000',
            '011100000111100000110000000110011111111111111011111111000011111000011111000011111000011111000011111000000000000000000000000000']

description = ['Locked','Unlocked']

# Configure Pi serial port
s = serial.Serial()
s.baudrate = 9600
s.timeout = 0
s.port = "/dev/ttyAMA0"

try:
    # Open serial port
    s.open()
except serial.SerialException, e:
    # There was an error
    sys.stderr.write("could not open port %r: %s\n" % (port, e))
    sys.exit(1)

print "Serial port ready"

# Clear display
s.write("$$$ALL,OFF\r")

loop = True

frame = 0

while loop:

    s.write('$$$F' + paddlock[frame] + '\r')
    print description[frame]

    inp = raw_input("Press [Enter] to toggle paddlock. [x-Enter] to quit.")

    if inp.lower()!="x":
      frame = 1 - frame
    else:
      loop = False

print "Good bye"