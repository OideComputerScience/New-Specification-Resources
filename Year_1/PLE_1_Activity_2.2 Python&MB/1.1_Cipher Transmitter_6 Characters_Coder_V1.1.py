# VER 1.1
# LCCS Team
# Event: PLE 1 Caeser Cipher Activity 2.2
# Purpose: A program that shifts each letter of a 6 letter word by 1
# Example: "Python" becomes "Qzuipo".

#Allows Python to communicate with the micro:bit through the USB serial connection
import serial
#control timing in programs
import time

port ='COM5'#change accordingly

MessageToBeCoded = input("Enter any 6 letter word: ")

#CaesarCipher To code message
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
  


