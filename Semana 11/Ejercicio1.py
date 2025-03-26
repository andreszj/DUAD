import math

class Circle:
    def get_area(self,radius):
        self.radius = radius 
        return self.radius*self.radius*math.pi
        

area = Circle()

print (f'Area del circulo 1 es: {area.get_area(5)}')
print (f'Area del circulo 2 es: {area.get_area(2)}')