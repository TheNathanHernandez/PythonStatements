from ess import ask 

number = ask("Guess a number between 1 and 20.")

while number != 12:
    if number > 12:
        print("Number is too high to be the answer.")
    if number < 12:
        print("Number is way too low to be the answer.")
    print('Wrong number. Try again.')
    number = ask("Guess a number between 1 and 20.")
print("Great job, you got 12.") 

