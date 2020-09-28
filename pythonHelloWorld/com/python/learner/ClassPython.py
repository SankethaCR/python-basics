class Point:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self):
        print("Move")


    def draw(self):
        print("Draw")


point1=Point(10,20)
point1.move()
point1.draw()

#point1.x=10
#point1.y=20

#print(f' {point1.x}*{point1.y}')
print(point1.x)
print(point1.y)
point1.x=30
print(f'Updated point1.x = {point1.x}')