import math

class Circle:
    def get_area(self,radius):
        self.radius = radius 
        return self.radius*self.radius*math.pi
        

area = Circle()

print (f'Circle Area: {area.get_area(5)}')