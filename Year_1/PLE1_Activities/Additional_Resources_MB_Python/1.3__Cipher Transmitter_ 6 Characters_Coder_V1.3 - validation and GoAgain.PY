# VER 1.3
# LCCS Team
# Event: PLE 1 Caeser Cipher Activity 2.2
# Purpose: A program that shifts each letter of a 6 letter word by 1
# The code validates text to be coded: it must be 6 cahracters long and no blanks
# The user can run the code until they decide to stop
# Example: "Python" becomes "Qzuipo".

#Allows Python to communicate with the micro:bit through the USB serial connection
import serial
#control timing in programs
import time

port ='COM5'#change accordingly

#Connecting to MB
microbit = serial.Serial(port, 115200)
time.sleep(2)  # allow connection to establish

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

#validation code to catch erroneous entries
#Initialise the loop guard variable
keepGoing  = True

# Loop as long as keepGoing is True
while keepGoing:
    
    #Inputting 6 characters to be coded
    MessageToCode = input("Enter any 6 letter word: ")
    
    if(len(MessageToCode)!=6 or MessageToCode==""):
        print("Message has to be 6 charters long an no blank message please.")
        continue   # go back to start of loop
        
        
    #Calling Function that codes the message
    result=caesarCipher(MessageToCode)

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
