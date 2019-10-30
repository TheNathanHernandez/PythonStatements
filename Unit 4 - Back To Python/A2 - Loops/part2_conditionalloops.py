from ess import ask 

print("Enter two numbers that equal 10")
num1 = ask("First number?")
num2 = ask("Second number?")

while num1 + num2 != 10:
  print("Try again")
  num1 = ask("First number?")
  num2 = ask("Second number?")
  
print("Good job!")