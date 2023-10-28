#area & perimeter of a circle in class circle
class Circle:
    def __init__(self,r,pi):
        self.r=r
        self.pi=pi
    def getarea(self):
        area=self.pi*self.r*self.r
        return area
    def getperimeter(self):
        perimeter=self.pi*self.r*2
        return perimeter
C=Circle(70, 22/7)
print(C.getarea())
print(C.getperimeter())
