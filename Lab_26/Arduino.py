import serial 
import time

arduino = serial.Serial(port ='COM15', baudrate = 9600, timeout =1)  
time.sleep(2) 

def send_command(command):
    arduino.write(command.encode())
    print(f"Sent: {command}")

while True:
    user_input = input("Enter 1 or 0 to send to Arduino (or 'exit' to quit): ")
    if user_input in ['1', '0']:
        send_command(user_input)
    elif user_input == 'q':
        print("Exiting...")
        break
    else:
        print("Invalid input. Please enter '1', '0', or 'exit'.")
