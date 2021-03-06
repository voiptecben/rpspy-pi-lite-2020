#!/usr/bin/env python


import serial, time, sys


s = serial.Serial()
s.baudrate = 9600
s.timeout = 0
s.port = "/dev/serial0"

try:
    s.open()
except serial.SerialException, e:
    sys.stderr.write("could not open port %r: %s\n" % (s.port, e))
    sys.exit(1)

s.write("$$$ALL,OFF\r")
time.sleep(0.2)
s.write("$$$B1,15\r")
time.sleep(0.2)
s.write("$$$B2,15\r")
s.write("$$$B1,25\r")
time.sleep(0.2)
s.write("$$$B3,15\r")
s.write("$$$B2,25\r")
s.write("$$$B1,50\r")
time.sleep(0.2)
s.write("$$$B4,15\r")
s.write("$$$B3,25\r")
s.write("$$$B2,50\r")
s.write("$$$B1,75\r")
time.sleep(0.2)
s.write("$$$B5,15\r")
s.write("$$$B4,25\r")
s.write("$$$B3,50\r")
s.write("$$$B2,75\r")
s.write("$$$B1,100\r")
time.sleep(0.2)
s.write("$$$B6,15\r")
s.write("$$$B5,25\r")
s.write("$$$B4,50\r")
s.write("$$$B3,75\r")
s.write("$$$B2,100\r")
s.write("$$$B1,100\r")
time.sleep(0.2)
s.write("$$$B7,15\r")
s.write("$$$B6,25\r")
s.write("$$$B5,50\r")
s.write("$$$B4,75\r")
s.write("$$$B3,100\r")
s.write("$$$B2,100\r")
s.write("$$$B1,75\r")
time.sleep(0.2)
s.write("$$$B8,15\r")
s.write("$$$B7,25\r")
s.write("$$$B6,50\r")
s.write("$$$B5,75\r")
s.write("$$$B4,100\r")
s.write("$$$B3,100\r")
s.write("$$$B2,75\r")
s.write("$$$B1,50\r")
time.sleep(0.2)
s.write("$$$B9,15\r")
s.write("$$$B8,25\r")
s.write("$$$B7,50\r")
s.write("$$$B6,75\r")
s.write("$$$B5,100\r")
s.write("$$$B4,100\r")
s.write("$$$B3,75\r")
s.write("$$$B2,50\r")
s.write("$$$B1,25\r")
time.sleep(0.2)
s.write("$$$B10,15\r")
s.write("$$$B9,25\r")
s.write("$$$B8,50\r")
s.write("$$$B7,75\r")
s.write("$$$B6,100\r")
s.write("$$$B5,100\r")
s.write("$$$B4,75\r")
s.write("$$$B3,50\r")
s.write("$$$B2,25\r")
s.write("$$$B1,15\r")
time.sleep(0.2)
s.write("$$$B11,15\r")
s.write("$$$B10,25\r")
s.write("$$$B0,50\r")
s.write("$$$B8,75\r")
s.write("$$$B7,100\r")
s.write("$$$B6,100\r")
s.write("$$$B5,75\r")
s.write("$$$B4,50\r")
s.write("$$$B3,25\r")
s.write("$$$B2,15\r")
s.write("$$$B1,25\r")
time.sleep(0.2)
s.write("$$$B12,15\r")
s.write("$$$B11,25\r")
s.write("$$$B10,50\r")
s.write("$$$B9,75\r")
s.write("$$$B8,100\r")
s.write("$$$B7,100\r")
s.write("$$$B6,75\r")
s.write("$$$B5,50\r")
s.write("$$$B4,25\r")
s.write("$$$B3,15\r")
s.write("$$$B2,25\r")
s.write("$$$B1,50\r")
time.sleep(0.2)
s.write("$$$B13,15\r")
s.write("$$$B12,25\r")
s.write("$$$B11,50\r")
s.write("$$$B10,75\r")
s.write("$$$B9,100\r")
s.write("$$$B8,100\r")
s.write("$$$B7,75\r")
s.write("$$$B6,50\r")
s.write("$$$B5,25\r")
s.write("$$$B4,15\r")
s.write("$$$B3,25\r")
s.write("$$$B2,50\r")
s.write("$$$B1,75\r")
time.sleep(0.2)
s.write("$$$B14,15\r")
s.write("$$$B13,25\r")
s.write("$$$B12,50\r")
s.write("$$$B11,75\r")
s.write("$$$B10,100\r")
s.write("$$$B9,100\r")
s.write("$$$B8,75\r")
s.write("$$$B7,50\r")
s.write("$$$B6,25\r")
s.write("$$$B5,15\r")
s.write("$$$B4,25\r")
s.write("$$$B3,50\r")
s.write("$$$B2,75\r")
s.write("$$$B1,100\r")
time.sleep(0.2)
s.write("$$$B14,25\r")
s.write("$$$B13,50\r")
s.write("$$$B12,75\r")
s.write("$$$B11,100\r")
s.write("$$$B10,100\r")
s.write("$$$B9,75\r")
s.write("$$$B8,50\r")
s.write("$$$B7,25\r")
s.write("$$$B6,15\r")
s.write("$$$B5,25\r")
s.write("$$$B4,50\r")
s.write("$$$B3,75\r")
s.write("$$$B2,100\r")
s.write("$$$B1,100\r")
time.sleep(0.2)
s.write("$$$B14,50\r")
s.write("$$$B13,75\r")
s.write("$$$B12,100\r")
s.write("$$$B11,100\r")
s.write("$$$B10,75\r")
s.write("$$$B9,50\r")
s.write("$$$B8,25\r")
s.write("$$$B7,15\r")
s.write("$$$B6,25\r")
s.write("$$$B5,50\r")
s.write("$$$B4,75\r")
s.write("$$$B3,100\r")
s.write("$$$B2,100\r")
s.write("$$$B1,75\r")
time.sleep(0.2)
s.write("$$$B14,75\r")
s.write("$$$B13,100\r")
s.write("$$$B12,100\r")
s.write("$$$B11,75\r")
s.write("$$$B10,50\r")
s.write("$$$B9,25\r")
s.write("$$$B8,15\r")
s.write("$$$B7,25\r")
s.write("$$$B6,50\r")
s.write("$$$B5,75\r")
s.write("$$$B4,100\r")
s.write("$$$B3,100\r")
s.write("$$$B2,75\r")
s.write("$$$B1,50\r")
time.sleep(0.2)
s.write("$$$B14,100\r")
s.write("$$$B13,100\r")
s.write("$$$B12,75\r")
s.write("$$$B11,50\r")
s.write("$$$B10,25\r")
s.write("$$$B9,15\r")
s.write("$$$B8,25\r")
s.write("$$$B7,50\r")
s.write("$$$B6,75\r")
s.write("$$$B5,100\r")
s.write("$$$B4,100\r")
s.write("$$$B3,75\r")
s.write("$$$B2,50\r")
s.write("$$$B1,25\r")
time.sleep(0.2)
s.write("$$$B14,100\r")
s.write("$$$B13,75\r")
s.write("$$$B12,50\r")
s.write("$$$B11,25\r")
s.write("$$$B10,15\r")
s.write("$$$B9,25\r")
s.write("$$$B8,50\r")
s.write("$$$B7,75\r")
s.write("$$$B6,100\r")
s.write("$$$B5,100\r")
s.write("$$$B4,75\r")
s.write("$$$B3,50\r")
s.write("$$$B2,25\r")
s.write("$$$B1,15\r")
time.sleep(0.2)
s.write("$$$B14,75\r")
s.write("$$$B13,50\r")
s.write("$$$B12,25\r")
s.write("$$$B11,15\r")
s.write("$$$B10,25\r")
s.write("$$$B9,50\r")
s.write("$$$B8,75\r")
s.write("$$$B7,100\r")
s.write("$$$B6,100\r")
s.write("$$$B5,75\r")
s.write("$$$B4,50\r")
s.write("$$$B3,25\r")
s.write("$$$B2,15\r")
s.write("$$$B1,0\r")
time.sleep(0.2)
s.write("$$$B14,50\r")
s.write("$$$B13,25\r")
s.write("$$$B12,15\r")
s.write("$$$B11,25\r")
s.write("$$$B10,50\r")
s.write("$$$B9,75\r")
s.write("$$$B8,100\r")
s.write("$$$B7,100\r")
s.write("$$$B6,75\r")
s.write("$$$B5,50\r")
s.write("$$$B4,25\r")
s.write("$$$B3,15\r")
s.write("$$$B2,0\r")
time.sleep(0.2)
s.write("$$$B14,25\r")
s.write("$$$B13,15\r")
s.write("$$$B12,25\r")
s.write("$$$B11,50\r")
s.write("$$$B10,75\r")
s.write("$$$B9,100\r")
s.write("$$$B8,100\r")
s.write("$$$B7,75\r")
s.write("$$$B6,50\r")
s.write("$$$B5,25\r")
s.write("$$$B4,15\r")
s.write("$$$B3,0\r")
time.sleep(0.2)
s.write("$$$B14,15\r")
s.write("$$$B13,25\r")
s.write("$$$B12,50\r")
s.write("$$$B11,75\r")
s.write("$$$B10,100\r")
s.write("$$$B9,100\r")
s.write("$$$B8,75\r")
s.write("$$$B7,50\r")
s.write("$$$B6,25\r")
s.write("$$$B5,15\r")
s.write("$$$B4,0\r")
time.sleep(0.2)
s.write("$$$B14,25\r")
s.write("$$$B13,50\r")
s.write("$$$B12,75\r")
s.write("$$$B11,100\r")
s.write("$$$B10,100\r")
s.write("$$$B9,75\r")
s.write("$$$B8,50\r")
s.write("$$$B7,25\r")
s.write("$$$B6,15\r")
s.write("$$$B5,0\r")
time.sleep(0.2)
s.write("$$$B14,50\r")
s.write("$$$B13,75\r")
s.write("$$$B12,100\r")
s.write("$$$B11,100\r")
s.write("$$$B10,75\r")
s.write("$$$B9,50\r")
s.write("$$$B8,25\r")
s.write("$$$B7,15\r")
s.write("$$$B6,0\r")
time.sleep(0.2)
s.write("$$$B14,75\r")
s.write("$$$B13,100\r")
s.write("$$$B12,100\r")
s.write("$$$B11,75\r")
s.write("$$$B10,50\r")
s.write("$$$B9,25\r")
s.write("$$$B8,15\r")
s.write("$$$B7,0\r")
time.sleep(0.2)
s.write("$$$B14,100\r")
s.write("$$$B13,100\r")
s.write("$$$B12,75\r")
s.write("$$$B11,50\r")
s.write("$$$B10,25\r")
s.write("$$$B9,15\r")
s.write("$$$B8,0\r")
time.sleep(0.2)
s.write("$$$B14,100\r")
s.write("$$$B13,75\r")
s.write("$$$B12,50\r")
s.write("$$$B11,25\r")
s.write("$$$B10,15\r")
s.write("$$$B9,0\r")
time.sleep(0.2)
s.write("$$$B14,75\r")
s.write("$$$B13,50\r")
s.write("$$$B12,25\r")
s.write("$$$B11,15\r")
s.write("$$$B10,0\r")
time.sleep(0.2)
s.write("$$$B14,50\r")
s.write("$$$B13,25\r")
s.write("$$$B12,15\r")
s.write("$$$B11,0\r")
time.sleep(0.2)
s.write("$$$B14,25\r")
s.write("$$$B13,15\r")
s.write("$$$B12,0\r")
time.sleep(0.2)
s.write("$$$B14,15\r")
s.write("$$$B13,0\r")
time.sleep(0.2)
s.write("$$$B14,0\r")






