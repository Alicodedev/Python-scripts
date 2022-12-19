# user input 4 bit binary decimal 
put = int(input("enter a 4 bit decimal number"))

# algorithm 
# use x % 2 by the input x

binary = [] # stores each modulus into a list append's it


for i in range(1):
      
# keep doing it till it hit's zero 
    
    # contain's the integer which will be used to find the reminder
    x = int(put/2) # 7/2 = 3.5
    x2 = (put%2) #x2 hold's the binary digit
    binary.append(x2) # stores binary digit into binary list
    
    y = int(x/2) # 3/2 = 1.5  r1 , x = 3 , 3%2
    y2 = (x%2) # y2
    binary.append(y2) # stores binary digit into binary list
   
    
    z = int(y/2) # 1/2 = 0.5 r1 , y = 1 , 1 %2
    z2 = (y%2) # z2 holds the binary digit 
    binary.append(z2) # stores binary digit into binary list
    
    a = z 
    a2 = (a%2) #stores binary digit into binary list
    print(a)
    
    binary.append(a2) # stores binary digit into binary list
    binary.reverse() #reverses the list for the right order in binary 
    
    
print(binary)    


