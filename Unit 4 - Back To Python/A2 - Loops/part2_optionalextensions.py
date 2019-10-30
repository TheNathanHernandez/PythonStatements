from ess import ask 

number = ask("Enter a number.")
total = number  
 
while total < 20: 
    print("Enter another number.")
    number = ask("Enter a number.")
    total = total + number
print("Congrats! You got over 20!")