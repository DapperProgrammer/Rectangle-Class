from RectangleClass import Rectangle

def main():

  # Sets "programStart" as an object of the Rectangle Class, which allows us to use this object
  # to call the Rectangle Class and all its attributes by using the programStart.insertAttributeNameHere mthod
  # Using "ProgramStart" Calls the class 'Rectangle' and stores '1' and '2' in 'width' and 'length'
  programStart = Rectangle(1, 2)
  print('Your starting width is:', programStart.width, 'and your starting length is:', programStart.length)
  print('Therefore your width is:', programStart.get_area(), 'and your length is:', programStart.get_perimeter())

  myVar = programStart.set_width(8)
  print(myVar)
  
  while True:
    try:
      # Uses "user" as an object of the Rectangle Class this time, allowing the user to set
      # a desired width and height (length). Remember to ask for the correct variables in order!
      # the order is whatever comes first in the class, in this case width comes before height(length)
      # so here we ask for width first. This ensures we get the correct values for the variables. 
      user = Rectangle (int(input('Now you try! Enter a width: ')), int(input('Enter a height: ')))
    except:
      print('Not an integer!')
    else:
      # Calls the function "get_area" and " get_perimeter" found in the Rectangle Class
      # These functions are set equal to whatever the value of the return statement in that specified function is. 
      print ('Area of the rectangle is:', user.get_area())
      print ('Perimeter of the rectangle is:', user.get_perimeter())
      break #stops the loop

main()
