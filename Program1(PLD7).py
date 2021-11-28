#Program 1:
#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8
print("\n\033[34;4mCounting Number of Words, Vowels and Consonants\033[0m")
user = input("\n>>\033[32;1mEnter a Sentence\033[0m: ")

def num_of_words():
    words = user.split()
    number_of_words = len(words)
    print(f"\n\033[31;1mNumber of Words\033[0m: {number_of_words}")

def num_of_vowels():
    count = 0
    vowel = set("aeiouAEIOU")

    for num in user:
        if num in vowel:
            count = count + 1
    print(f"\033[31;1mNumber of Vowels\033[0m: {count}")

def num_of_consonants():
    count = 0
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

    for _num in user:
        if _num in consonants:
            count = count + 1
    print(f"\033[31;1mNumber of Consonants\033[0m: {count}")

num_of_words()
num_of_vowels()
num_of_consonants()

