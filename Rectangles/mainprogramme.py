from Geometry_Package import *
from Tkinter import *
import sys

#Defining functions
#Defining shape selector function which will generate the appropriate object the user selects
def shapeselector(user_input):
    if (user_input=='square')or (user_input=='Square'):
        user_shape=square()

    elif(user_input=='rectangle') or (user_input=='Rectangle'):
        user_shape=Rectangle()
        
    elif(user_input=='circle') or (user_input=='Circle'):
        user_shape=circle()

    else:
        user_shape='You have entered an invalid shape. Please try again.'
    
    return user_shape

#Beginning of actual programme

#Welcome message
print " "
print "Welcome to the geometry manager. At any time, enter 9 to end the programme."

menu_selection=0

while (menu_selection != '9'):
    #Presentation of options
    print " "
    print "Please select an action you would like to perform from the list below and enter the corresponding number to continue:"
    print "1. Create new shape"
    print "2. See specifications of current shape"
    print "3. Set specifications of current shape"
    print "4. Calculate the area of current shape"
    print "5. Display positional co-ordinates of current shape"
    print "6. Move current shape to different co-ordinates"

    menu_selection=raw_input("")
    
    if (menu_selection=='1'):
        user_shape_choice=0
        user_shape='You have entered an invalid shape. Please try again.'
        
        user_shape_choice=raw_input("Please enter the type of shape you would like to create: ")
        user_shape=shapeselector(user_shape_choice)
        
        while (user_shape=='You have entered an invalid shape. Please try again.'):
            print user_shape
            user_shape_choice=raw_input("Please enter the type of shape you would like to create: ")
            user_shape=shapeselector(user_shape_choice)
        
        shape=user_shape.__class__.__name__
        print 'A', shape, 'has been created for you!'
    
    
    elif (menu_selection=='2'):
        user_shape.specs()
        
        
    elif (menu_selection=='3'):
        shape=user_shape.__class__.__name__
        if (shape=='square'):
            side=raw_input("Please enter the length of the side of the square: ")
            side=float(side)
            user_shape.setwidthandheight(side)
        
        elif (shape=='Rectangle'):
            width=raw_input("Please enter the length of the width: ")
            length=raw_input("Please enter the length of the length: ")
            width=float(width)
            length=float(length)
            user_shape.setwidthandheight(width, length)
            
        elif (shape=='circle'):
            radius=raw_input("Please enter the length of the radius: ")
            radius=float(radius)
            user_shape.setwidthandheight(radius)
            
    elif (menu_selection == '4'):
        user_shape.area()
        
    elif (menu_selection == '5'):
        user_shape.displaycoord()
    
    elif (menu_selection == '6'):
        xmove=raw_input("Please enter the amount by which you would like to move the shape along the x-axis: ")
        ymove=raw_input("Please enter the amount by which you would like to move the shape along the y-axis: ")
        user_shape.translate(xmove, ymove)
        
    elif(menu_selection != '9'):
        print "You have entered an invalid menu choice. Please try again."

sys.exit("You have chosen to exit the programme. Have a nice day")