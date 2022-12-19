#mathematical class Slope 


# class defined 

import numpy as np

class slope:
    # class body will contain self object properties
    # each properties is defined as varables for the operation of the methods
    def __init__(self,Y1,X1,X2,Y2):
        self.Y2 = Y2
        self.X2 = X2
        self.Y1 = Y1
        self.X1 = X1
        
    
    #class methods(functions) these methods will have a function and can use the properties 
    ## as the operations for them
    def rise_run(self):
        rise = (self.Y2 - self.Y1)
        run = (self.X2 - self.X1)
        total = rise / run 
        return total 


# can I give a list of X and Y values 

#####@@@@@@@@@@@@@ can  I make a loop to declare variables instead of manual declaritions 
y_2 = int(input("Enter y2 values")) 
y_1 = int(input("Enter y1 values"))
x_2 = int(input("Enter X2 values"))
x_1 = int(input("Enter X1 values"))

num = slope(y_2,y_1,x_2,x_1) # inputing all the values for the slope 

print(num.rise_run()) #calling the method to do the operation for the inputed values
