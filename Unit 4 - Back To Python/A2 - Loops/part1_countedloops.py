from ess import ask

print("FIRST LOOP")
for i in range(5):
  print("Hello")

print("")
print("SECOND LOOP")
for j in range(3):
  print("j =", j)

print("")
print("THIRD LOOP")
for i in range(6, 10):
  print("i =", i)

print("")
print("ADDER")
total = 1
for i in range(4):
  num = ask("Enter a number:")
  total * num 
print("The numbers add to", total)

word = ask("Enter a random word.")
number = ask("Enter a number. This will be used later in the program.")

for i in range(number):
  print(word)
print("Your word has been successfully printed", number, "times.")