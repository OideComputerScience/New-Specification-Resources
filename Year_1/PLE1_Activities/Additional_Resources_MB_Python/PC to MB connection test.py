# Event:PLE 1 
# Purpose: To test to see if active port will have serial communcation with a MicroBit
# LCCS Team

import serial
import time

# Replace with your micro:bit port
# Windows example: 'COM3'

port = 'COM5'

microbit = serial.Serial(port, 115200)
time.sleep(2)  # allow connection to establish

microbit.write(b"Hi\n")

microbit.close()

print("FIN")