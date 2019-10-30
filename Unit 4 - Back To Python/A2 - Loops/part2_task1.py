from ess import ask 

number = ask("Enter a number less than 10.")

while number >= 10: 
    print("Try again.")
    number = ask("Enter a number less than 10.")
print("You found a number less than 10. Thanks for using the program!")