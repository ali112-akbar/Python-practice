import re

def validate_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        return True
    else:
        return False
    
email = input("Enter a email adress")
if validate_email(email):
    print("The email adress is valid")
else:
    print("The email adress in in valid")