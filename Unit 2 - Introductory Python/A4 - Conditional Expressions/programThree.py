# Program 3
# Code: Nathan Hernandez

from ess import ask 

number = ask("Choose a number.")
numberTwo = ask("Choose a second number.")
numberThree = ask("Choose a third number.")

if number > numberTwo and numberThree:
    print(number,"is higher than",numberTwo,"and",numberThree)


if numberTwo > number and numberThree: 
    print(numberTwo,"is higher than",number,"and",numberThree)

if numberThree > numberTwo and number:
    print(numberThree,"is higher than",numberTwo,"and",number)

