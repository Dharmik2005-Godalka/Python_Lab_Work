import re

def pan(pan):
    pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if re.match(pattern, pan):
        return True
    return False

number = input("Enter PAN number: ")

if pan(number):
    print("Valid PAN number.")
else:
    print("Invalid PAN number.")
