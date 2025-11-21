import re

def email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

email_id = input("Enter email ID: ")

if email(email_id):
    print("Valid email ID.")
else:
    print("Invalid email ID.")
