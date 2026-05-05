# LCCS Team
# Event: PLE 1 Caeser Cipher
# Purpose:To transmit a  6 charcter message to a micr:bit that
# transmeit the message to a recieving micro:bit
# A program using a caeser cipher key of 1
# Example: "Python" becomes "Qzuipo".


#Allows Python to communicate with the micro:bit through the USB serial connection
import serial
#control timing in programs
import time

port ='COM22'#Run "Finding_a_port.py" to find a port on your computer and change accordingly

MessageToBeCoded = input("Enter any 6 letter word: ")

#Using a Caeser cipher key of 1 to code message
codedStr = chr(ord(MessageToBeCoded[0])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[1])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[2])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[3])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[4])+1)
codedStr = codedStr + chr(ord(MessageToBeCoded[5])+1)
print(codedStr)

#Connecting to MB
microbit = serial.Serial(port, 115200)
time.sleep(2)  # allow connection to establish

#String encode() method in used to convert a
#string into bytes using a specified encoding format.

microbit.write(f"{codedStr}\n".encode())
              
microbit.close()
  


