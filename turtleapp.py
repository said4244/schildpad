import turtle
schild = turtle.Turtle()
scherm = turtle.Screen()
scherm.title('TurtleApp')
schild.shape('turtle')
schild.speed(100)
schild.color('red', 'green')
turtle.bgcolor('black')
def circels():
    for i in range(36):
        schild.forward(10)
        schild.right(10)
kleuren_lijst = ["red", "yellow", "green", "blue", "purple", "orange"]
for iets in kleuren_lijst:
    schild.color(iets, 'green')
    circels()
    schild.left(60)
schild.left(180)
schild.color('gold', 'green')
for i in range(50):
    schild.width(1)
    schild.forward(5)
for i in range(36):
    for i in range(36):
        schild.forward(10)
        schild.left(10)
    schild.left(10)
schild.color('red', 'green')
schild.left(180)
for i in range(50):
    schild.width(1)
    schild.forward(13)
def polygon(n):
    for i in range(n):
        schild.forward(50)
        schild.left(360/n)
for i in range(3, 24):
    polygon(i)
    schild.left(30)
scherm.mainloop()
