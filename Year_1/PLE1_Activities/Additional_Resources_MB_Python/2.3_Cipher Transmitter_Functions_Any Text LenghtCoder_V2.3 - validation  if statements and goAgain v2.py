# Ver 2.3
# LCCS Team
# Event: PLE 1 Caeser Cipher Activity 2.2
# Purpose: A program that shifts each letter of a 6 letter word by 1
# Purpose: Demo Caeser Cipher using lists to overcome size of text to be coded
# Allow user to send multiple messages

#Allows Python to communicate with the micro:bit through the USB serial connection
import serial
#control timing in programs
import time

port="COM5"#change accordingly

#Connecting to MB
microbit = serial.Serial(port, 115200)
time.sleep(2)  # allow connection to establish

#Method to code message
def caesarCipher(ToCode):
    codedStr = chr(ord(ToCode[0])+1)#first character already 
    
    for i in range (len(ToCode)-1):#first character already coded
        codedStr = codedStr + chr(ord(ToCode[i+1])+1)
    print(codedStr)#to see coded message in shell
    return codedStr


#Validation that an empty string has not been entered
#This code will check if the string is empty, if so it
#gives the user a message and offer the user a chance
#to enter another message or quit.

#Initialiseing the loop guard
keepGoing=True

while keepGoing:

    #Inputting message to be coded
    MessageToBeCoded = input("Enter message to be coded: ")

    if (MessageToBeCoded ==""):
        print("No blank message please.")
        continue   # go back to start of loop
    
    # Convert message to list of characters
    MessageToBeCodedList = list(MessageToBeCoded)

    #Calling Function that codes the message
    result=caesarCipher(MessageToBeCodedList)
    
    #String encode() method in used to convert a
    #string into bytes using a specified encoding format.
    microbit.write(f"{result}\n".encode())
    
    # Ask user if they want to go again
    keepGoing= input("Would you like to code more text, Y/N:  ")
                      
    if keepGoing.upper() == "N":
        keepGoing = False
        
# Closing MB connection
microbit.close()   
print("Goodbye")

