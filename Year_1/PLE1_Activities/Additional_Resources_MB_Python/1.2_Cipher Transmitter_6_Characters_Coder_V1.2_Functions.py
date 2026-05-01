# VER 1.2
# LCCS Team
# Event: PLE 1 Caeser Cipher Activity 2.2
# Purpose: A program that shifts each letter of a 6 letter word by 1
# Example: "Python" becomes "Qzuipo".

#Allows Python to communicate with the micro:bit through the USB serial connection
import serial
#control timing in programs
import time

port ='COM5'#change accordingly

#Method to code message
def caesarCipher(MessageToCode):
    codedStr = chr(ord(MessageToCode[0])+1)
    codedStr = codedStr + chr(ord(MessageToCode[1])+1)
    codedStr = codedStr + chr(ord(MessageToCode[2])+1)
    codedStr = codedStr + chr(ord(MessageToCode[3])+1)
    codedStr = codedStr + chr(ord(MessageToCode[4])+1)
    codedStr = codedStr + chr(ord(MessageToCode[5])+1)
    print(codedStr)
    return codedStr

#Inputting message to be coded
MessageToBeCoded = input("Enter any 6 letter word: ")

#Calling Function that codes the message
result=caesarCipher(MessageToBeCoded)


#Connecting to MB
microbit = serial.Serial(port, 115200)
time.sleep(2)  # allow connection to establish

#String encode() method in used to convert a
#string into bytes using a specified encoding format.

microbit.write(f"{result}\n".encode())
#microbit.write(b"hi\n")               
microbit.close()



