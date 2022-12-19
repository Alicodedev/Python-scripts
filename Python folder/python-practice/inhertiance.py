class vehicle:
    def general_useage(self):
        print('General use: transporation')
        
class Car(vehicle): # sub class using vehicle class as template
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True
    
    def specific_usage(self):
        print("specific use: commute to work,  vaction with family")
    
class motor(vehicle): # sub class using vehicle as template 
    def __init__(self):
        print("I'm motor cycle")
        self.wheels = 2
        self.has_roof = False 
        
    def specific_usage(self):
        print("specific use: road trip, racing")
        
c = Car()
c.general_useage() # able to call parent method becuase its inherited.

print(isinstance(c,Car)) #built in fucntion checking if c is is an object of class Car

        
        
        




# can you use the format of a class to create another class with modifed properties