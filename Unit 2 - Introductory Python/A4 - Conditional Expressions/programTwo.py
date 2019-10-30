# Program 2
# Code: Nathan Hernandez
from ess import ask 

number = ask("Enter a number between 10 and 20.")

if number < 10:
    print("This number is lower than 10. Please pick a higher number.")

if number > 20:
    print("This number is higher than the requested limit. Please pick a number between 10 and 20.")

if number >= 10 and number <= 20:
    print("Congratulations! You picked a number between 10 and 20. Awesome!")