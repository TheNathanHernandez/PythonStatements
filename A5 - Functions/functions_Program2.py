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
    diamond()
    bigDiamond()

diamond()
bigDiamond()
triangle()