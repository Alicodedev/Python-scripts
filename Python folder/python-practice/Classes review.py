  
#@@ questions: can you have methods with methods such as functions within functions

class Human:
    def __init__(self,name,work): # __init__ allows the properties of class to exist
        self.name = name 
        self.work = work
       
    def do_work(self): # method defined to do operation with the properties of the class
        # behaviours of the object are defined in the method 
        
        if self.work == "tennis player":
            print(self.name,"playes tennis")
            
        elif self.work == "actor":
            print(self.name,"does acting")
    
#tom = Human("tom","actor") # define the object with the properties of the class 

#tom.do_work()# using the defiend object to operate with the method


    
    # what proptires does the class contain
    
    # what methods will the object take 


        