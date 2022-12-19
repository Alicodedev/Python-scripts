class Square:
     def __init__(self, side):
         self.side = side
  
     def area(self):
         return self.side * self.side
  
class Cube(Square):
      def area(self):
         face_area = self.side * self.side
         return face_area * 6
  
      def volume(self):
         face_area = self.side * self.side
         return face_area * self.side
     


bob = Square(6) # define the argument's for the properties of the class by using __init__

bob.side # call the method which you're using 

print(bob.area())




