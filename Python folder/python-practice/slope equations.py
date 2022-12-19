# function with parameter of the quation ax + b = c
# each parmeter will be equal to inputs of an equation a = input b = input etc 
# this function will have operations to solve an equation for X 

# equation inputs
a_in = int(input("enter a number for a"))
b_in = int(input("enter a number for b"))
c_in = int(input("enter a number for c"))

## function definition 
def Equation(a = a_in, b = b_in , c = c_in ):
    # Equation(input parameters)

## function body
    # make variable for each term and do opeartions on them
    Ax_b = a_in + (b_in-b_in)
    
    C_ =  c_in - b_in
    
    Ax_b_C =  C_  / Ax_b
    
    return Ax_b_C
    
print(Equation()) 


### use this simple concept as layout for further formation