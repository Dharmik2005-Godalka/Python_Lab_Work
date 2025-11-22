import serial
import time

PORT = "COM3" 
BAUD = 9600

try:
    arduino = serial.Serial(PORT, BAUD, timeout=1)
    time.sleep(2) 

    message = "Hello Arduino!"
    arduino.write(message.encode()) 
    print("Message sent:", message)

    arduino.close()

except Exception as e:
    print("Error:", e)
