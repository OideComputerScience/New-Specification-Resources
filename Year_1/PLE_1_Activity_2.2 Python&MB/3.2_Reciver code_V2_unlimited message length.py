# Event: PLE 1 Caeser Cipher Activity 2.2 - Reciever decoding script V2
# LCCS Team
# Purpose: To receive coded data of any character length
# from a Micro:Bit and to output the decoded message to the shell

# Allows Python to communicate with the micro:bit through the USB serial connection
import serial

port = "COM3"#change accordingly

ser = serial.Serial(port,115200,timeout=1)

print("Listening for MB messages...")

while True:
    if ser.in_waiting:
        codedMessage=ser.readline().decode('utf-8').strip()
        if codedMessage:
            #printing received code massage
            print("Recieved Code: ",codedMessage)
            #decoding message received
            
            #each string character placed in list
            MessageToBeDecodeList=list(codedMessage)
            #print coded masseg in shell
            print (MessageToBeDecodeList)
            
            #Decode the First Character
            deCodedMessage= chr(ord(MessageToBeDecodeList[0])-1)
           
            #Decode the Remaining Characters
            for i in range (len(MessageToBeDecodeList)-1):
               deCodedMessage = deCodedMessage + chr(ord(MessageToBeDecodeList[i+1])-1)
            print(deCodedMessage)

#Close MB connection
ser.close()