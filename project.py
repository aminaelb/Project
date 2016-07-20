import turtle
wn = turtle.Screen()
def setup(col, x, y, w, s, shape): 
    turtle.up()
    turtle.goto(x,y)
    turtle.width(s)
    turtle.turtlesize(s)
    #bgpic("https://d13yacurqjgara.cloudfront.net/users/375867/screenshots/1480136/game-assets-game-background-sidescroller.png")
    #bgpic("background.png")
    wn.bgcolor("blue")
    turtle.color(col)
    turtle.shape(shape)
    #turtle.down()
    wn.onkeypress(up, "Up")
    wn.onkeypress(left, "Left")
    wn.onkeypress(right, "Right")
    wn.onkeypress(back, "Down")
    wn.onkey(quitTurtles, "Escape")
    wn.listen()
    wn.mainloop()
 

#Event handlers
def up():
    #turtle.pendown()
    turtle.fd(20)
    #turtle.penup()
def left():
    turtle.lt(180)
    #turtle.fd(50)
def right():
    turtle.rt(180)
    #turtle.fd(50)
def back():
    turtle.bk(30)
 
def quitTurtles():
    wn.bye()

setup("green",-270,-270,2,2,"turtle")
