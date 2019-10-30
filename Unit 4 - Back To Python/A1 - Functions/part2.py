from ess import ask 
def rowOfOne():
  print("   *")

def rowOfThree():
  print("  ***")

def rowOfFive():
  print(" *****")

def rowOfSeven():
    print(" *******")

def diamond():
  rowOfOne()
  rowOfThree()
  rowOfFive()
  rowOfThree()
  rowOfOne()

def bigDiamond():
  rowOfOne()
  rowOfThree()
  rowOfFive()
  rowOfSeven()
  rowOfThree()
  rowOfOne()

def triangle():
  rowOfOne()
  rowOfThree()
  rowOfFive()
  rowOfThree()
  rowOfOne()
  rowOfOne()
  rowOfThree()
  rowOfFive()
  rowOfSeven()
  rowOfThree()
  rowOfOne()

def shapes():
    diamond()
    bigDiamond()
    triangle()

diamond()
bigDiamond()
triangle()
shapes()