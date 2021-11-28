#Program 1:
#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8

user = input("Enter a Sentence: ")

words = user.split()
number_of_words = len(words)
print(f"No. of words : {number_of_words}")

def num_of_vowels():
    count = 0
    vowel = set("aeiouAEIOU")

    for num in user:
        if num in vowel:
            count = count + 1
    print(f"No. of vowels :", count)

def num_of_consonants():
    count = 0
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

    for _num in user:
       if _num in consonants:
           count = count + 1
    print("No. of consonants :", count)

num_of_vowels()
num_of_consonants()

