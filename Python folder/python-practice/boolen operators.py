#AND operator
# function named and with 2 inputs x,y 
def AND(x,y):
    # body of the function checks if x and y are similar 
    if x and y == 1:
        return True 
    # else not identical  values therefore  false 
    else:
        return False 
    
    #Returns the value of x, y AND opeartions 
#print(AND(1,1))






# OR operator 
# function  name OR  with x and y inputs
def OR(x,y):
    # if x or y == 1 return 1 
    if x or y == 1:
        return True
    # else return 0
    else:
        return False 

#print(OR(,))





#NOT operator 
# function name NOT with x inputs single input
def NOT(x):
    
    # takes the oppostie value of the input
    if x == 1:
        return 0
    # if x is == 1 return 0
    else:
        return 1
    #else return 1 

print(NOT(0))  
