from ess import ask


def areaOfACircle(radius):

    radiusCode = 3.14 * (radius * radius)
    print(radiusCode)


def volumeOfACube(side):
    cubeCalculation = (side * side * side)
    print(cubeCalculation)


def perimeterOfATriangle(side1, side2, side3):
    calculationTriangle = (side1 + side2 + side3)
    print(calculationTriangle)

# Don't edit anything below here. It will print a menu to allow
# the user to select which of your functions is run.
print("What do you want to calculate? ")
print("[1] The area of some circles")
print("[2] The volume of some cubes")
print("[3] The perimeter of some triangles")
print("")
choice = ask("Enter your selection: ")

if choice == 1:
    areaOfACircle(5)
    areaOfACircle(10)
    areaOfACircle(20)

if choice == 2:
    volumeOfACube(2)
    volumeOfACube(8)
    volumeOfACube(15)

if choice == 3:
    perimeterOfATriangle(2, 3, 4)
    perimeterOfATriangle(7, 8, 10)
    perimeterOfATriangle(25, 38, 43)
