# Event: PLE 1 Caeser Cipher Activity 2.2 - Reciever decoding script V1
# LCCS Team
# Purpose: To receive fixed coded data (6 characters) from a
# Micro:Bit and to output the decoded message to the shell

# Allows Python to communicate with the micro:bit through the USB serial connection
import serial

port = "COM3"#change accordingly

ser = serial.Serial(port,115200,timeout=1)

print("Listening for MB messages...")

while True:
    if ser.in_waiting:
        codedMessage=ser.readline().decode('utf-8').strip()
        if codedMessage:
            print("Recieved Code: ",codedMessage)
            #decoding message received
            deCodedMessage= chr(ord(codedMessage[0])-1)
            deCodedMessage = deCodedMessage + chr(ord(codedMessage[1])-1)
            deCodedMessage = deCodedMessage + chr(ord(codedMessage[2])-1)
            deCodedMessage = deCodedMessage + chr(ord(codedMessage[3])-1)
            deCodedMessage = deCodedMessage + chr(ord(codedMessage[4])-1)
            deCodedMessage = deCodedMessage + chr(ord(codedMessage[5])-1)
            
            # Print out decoded message
            print("The decoded message is: ",deCodedMessage)
#Close MB connection
ser.close()