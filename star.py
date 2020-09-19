import turtle as patel
import random as coder
def star (x , y , color , side):
    patel.color(color)
    patel.begin_fill()
    patel.penup()
    patel.goto(x,y)
    patel.pendown()
    for k in range(5):
        patel.forward(side)
        patel.right(144)
        patel.forward(side)
    patel.end_fill()
def randoml():
    return coder.randrange(5 , 25)
def randomll():
    return coder.randrange(-290 , 290) , coder.randrange(-270 , 270)
patel.title("star m")
patel.bgcolor("black")
patel.speed("fastest")
colors = ["red" , "orange" , "green" , "magenta" ,  "blue" , "yellow"]
stars= 60
for k in range (stars):
    color = coder.choice(colors)
    side = randoml()
    x , y = randomll()
    star(x,y,color,side)
patel.done()                    
