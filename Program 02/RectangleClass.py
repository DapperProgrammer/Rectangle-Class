# Calvin Tracy
# CS 222 02
# Program Assignment 02
# Due Date: 02/09/2018
# Date turned in: 02/09/2018
# Program for printing out the area and perimeter of a Rectangle
# https://www.youtube.com/watch?v=apACNr7DC_s&t=311s

# "init" method is called every time you careate a new instance of the class
# which is done by creating a new object of the class.

# "self" is a reference to an object crated to use the class.
# Every time you crate an object for a class, "self" is used as
# a reference variable to that object. "self = myObject"
# and also attaches variable names to the object of the class
# you must include "self" in order to use an object for a class
# if you don't include "self" in your methods then you cannot use that method
# with the object. Just like if you do not attatch "self" to your variables
# you cannot print those variables using the object.

# Another explanation of "self"
# https://pybit.es/python-classes.html
# Self is pretty self explanatory (pun intended!). It’s referring to itself.
# That is, the actual Person object that’s being created.
# Such as "myObject = Rectangle"
class Rectangle:
  def __init__(self, width, length):
    # "self.width" & "self.length" are the fields(methods) that store the value
    # to be used within the class and its methods.
    # "width" & "length" are variables provided by the user
    self.width = width
    self.length = length

  # The set methods are used to change the width/length individually.
  def set_width(self, width):
    self.width = width
    return self.width

  def set_length(self, length):
    self.length = length
    return self.length
    
  def get_area(self): # Assigns the variable self (and all arguments attached to it) to the function
    rectangle_area = self.width * self.length # 1 * 2 sets the answer to 'rectangle_area'
    return(rectangle_area) # Assigns the value of 1 * 2 to the function "get_area"
    
  def get_perimeter(self): # Assigns the variable self (and all arguments attached to it) to the function
    rectangle_perimeter = 2*(self.width + self.length) # 2 * (1 + 2)
    return(rectangle_perimeter) # Assigns the value of 2 * (1 + 2) to the function "get_perimeter"
