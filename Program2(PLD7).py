#Program 2: Password validator
#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex.
#input: P@ssw0rd+P@ssw0rd
#ouput: Valid

#Tip: loop through each character of the input then process it letter by letter

print(">>\33[32;1mPASSWORD VALIDATOR\33[0m<<")
user = input("\n\33[33;3mEnter your\33[0m \33[32;1mPASSWORD\33[0m: ")

def validator():
    spclChar = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ".", "|", ";", ":", "'", "?", ",", "/", "<", ">", "~", "`")
    val = True

    if len(user) < 16:
        print("\33[31;3mPassword length should be Greater than 15 letters.")
        val = False
    
    if not any(char.isdigit() for char in user):
        print("\33[31;3mPassword should have at least one number.")
        val = False
    
    if not any(char.isupper() for char in user):
        print("\33[31;3mPassword should have at least one capital letter.")
        val = False

    if not any(char in spclChar for char in user):
        print("\33[31;3mPassword should have at least one special character.\33[0m")
        val = False
    
    return val

def display():
    if (validator()):
        print("\33[32;1mPASSWORD\33[0m is \33[34;1mVALID\33[0m")

    else:
        print("\33[32;1mPASSWORD\33[0m is \33[31;1mINVALID\33[0m")

display()
