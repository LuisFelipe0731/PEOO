class Triangulo:
    def __init__(self):
        self.h = 0
        self.b = 0
    
    def Area_tri(self):
        return (self.b * self.h)/2

junior = Triangulo()
junior.h = 60

print(junior.b)