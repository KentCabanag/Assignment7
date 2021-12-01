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

user = input("Enter your PASSWORD: ")

def validator():
    spclChar = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ".", "|", ";", ":", "'", "?", ",", "/", "<", ">", "~", "`")
    val = True

    if len(user) < 15:
        print("\nLength should be greater than 15 letters")
        val = False
    
    if not any(char.isdigit() for char in user):
        print("Password should have at least one number")
        val = False
    
    if not any(char.isupper() for char in user):
        print("Password should have at least one capital letter")
        val = False

    if not any(char in spclChar for char in user):
        print("Password should have at least one special character")
        val = False
    
    return val


