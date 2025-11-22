import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1) 
time.sleep(2) 

while True:
    command = input("Enter command (ON/OFF): ").strip()
    if command in ["ON", "OFF"]:
        ser.write((command + '\n').encode()) 
        print(f"Sent: {command}")
    else:
        print("Invalid command. Enter ON or OFF.")

ser.close()
