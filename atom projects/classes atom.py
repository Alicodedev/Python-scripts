class Human:
    def __init__(self,name,work): # __init__ allows the properties of class to exist
        self.name = name
        self.work = work

    def do_work(self): # method defined to do operation with the properties of the class
        if self.work == "tennis player":
            print(self.name,"playes tennis")

        elif self.work == "actor":
            print(self.name,"does acting")

tom = Human("tom","actor") # define the object with the properties of the class

print(tom.do_work())# using the defiend o
