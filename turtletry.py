import turtle
p = turtle.Pen()
while True:
    x=1
    while x<15:
        x=x+1
        if x % 2 == 0:
            p.color("blue")
        else:
            p.color("red")
        p.forward(200)
        p.left(170)
    while x<30:
        x=x+1
        if x % 2 == 0:
            p.color("blue")
        else:
            p.color("red")
        p.forward(400)
        p.right(170)
