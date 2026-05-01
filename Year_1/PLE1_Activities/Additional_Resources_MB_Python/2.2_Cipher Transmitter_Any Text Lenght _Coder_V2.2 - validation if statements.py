# Ver 2.2
# LCCS Team
# Event: PLE 1 Caeser Cipher Activity 2.2
# Purpose: A program that shifts each letter of a 6 letter word by 1
# Purpose: Demo Caeser Cipher using lists to overcome size of text to be coded
# Using validation to idicate if an empty string has been entered
 
#Allows Python to communicate with the micro:bit through the USB serial connection
import serial
#control timing in programs
import time

port="COM5"#change accordingly


#Method to code message
def caesarCipher(ToCode):
    codedStr = chr(ord(ToCode[0])+1)#first character already 
    
    for i in range (len(ToCode)-1):#first character already coded
        codedStr = codedStr + chr(ord(ToCode[i+1])+1)
    print(codedStr)#to see coded message in shell
    return codedStr

#Validation that an empty string has not been entered
#This code will check if the string is empty, if so it
#gives the user a message and quit


#Inputting message to be coded
MessageToBeCoded = input("Enter message to be coded: ")

if (MessageToBeCoded !=""):
    #add message to code to list
    MessageToBeCodedList = list(MessageToBeCoded)

    #Calling Function that codes the message
    result=caesarCipher(MessageToBeCodedList)
    
    #Connecting to MB
    microbit = serial.Serial(port, 115200)
    time.sleep(2)  # allow connection to establish

    #String encode() method in used to convert a
    #string into bytes using a specified encoding format.
    microbit.write(f"{result}\n".encode())
    
    #closing MB connection
    microbit.close()
    
else:
    print("No blank space please, Goodbye")



