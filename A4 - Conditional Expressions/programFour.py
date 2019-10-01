# Program Four
# Code: Nathan Hernandez

from ess import ask 

letter = ask("Enter in a letter from A to F.")

if letter == "A" or letter == 'E': 
    print("You chose a vowel.")

if letter == 'B' or letter == 'C' and letter == 'D' and letter == 'F':
    print("You chose a consonant.")

if letter == 'A' or letter == 'B':
    print("According to the letter you gave to the console, you have a good grade!")
else: 
    print("Sorry, due to the letter you chose. You have a poor grade.")

if letter == 'C' or letter == 'A' or letter == 'N' or letter == 'D':
    print("The letter you picked is in the word Canada.")
else: 
    print("The letter you chose was not in the letter Canada, eh?")

if letter == 'A' or letter == 'E' or letter == 'F' or letter == 'N':
    print("This letter can be drawn without any curved lines.")
else: 
    print("This letter cannot be drawn without at least one or two curved lines.")