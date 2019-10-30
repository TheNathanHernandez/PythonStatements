# Example 1 - Draw a stick figure
def stickFigure():
  print("  0   ")
  print("--+-- ")
  print("  |   ")
  print(" / L ")

# Example 2 - Draw a nice ASCII heading, given a title
def header(title):
  print("===================================")
  print("   "+title)
  print("===================================")

# Example 3 - Calculate the area of a rectangle, given width and height
def areaOfARectangle(width, height):
  area = width * height
  print("The area of the rectangle is",area)

# Up to this point, our code will do absolutely nothing! To use the functions, we need
# to call them elsewhere in the program. Below, we call each of our three functions:

stickFigure()
header("An Awesome Python Program")
header("Testing the program!")
header("Here's another call!")
areaOfARectangle(3, 4)
areaOfARectangle(5, 5)
areaOfARectangle(6, 6)
areaOfARectangle(8, 8)
areaOfARectangle(8, 9)