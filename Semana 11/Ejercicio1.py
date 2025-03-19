class Circle:
    radius = 0
    def get_area(self,radius):
        self.area = radius*radius*3.14
        print(f'Este es el radio: {radius} y esta es el area del circulo {self.area}')

area1 = Circle ()
area2 = Circle ()
area1.radius = 5
area2.radius = 2
area1.get_area(area1.radius)
area2.get_area(area2.radius)