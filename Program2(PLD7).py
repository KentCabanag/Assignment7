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
def vowel_count(str):
      
    # Initializing count variable to 0
    count = 0
      
    # Creating a set of vowels
    vowel = set("aeiouAEIOU")
      
    # Loop to traverse the alphabet
    # in the given string
    for alphabet in str:
      
        # If alphabet is present
        # in set vowel
        if alphabet in vowel:
            count = count + 1
      
    print("No. of vowels :", count)
      
# Driver code 
str = "jhed aso pogi gwapo"
  
# Function Call
vowel_count(str)
