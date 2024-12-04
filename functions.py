import turtle as t 
t.speed(100)
t.bgcolor("blue")
def go (x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def rec (w,h,c):
    t.color(c)
    t.begin_fill()
    for i in range (2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

go(-200,-100)
rec(700,200,"#5c2903")

# grass

go(-200,100)
def grass (size,color):
    t.color(color)
    t.begin_fill()
    t.setheading(45)
    t.forward(size)
    t.right(90)
    t.forward(size)
    t.end_fill()
for i in range (20):
    grass (25,"green")

# tiny appartment

go(-200,100)
t.setheading(0)
rec(200,225,"orange")
go(-200,325)
grass (149,"#800000")

# door

go(-185,100)
rec(30,112.5,"brown")



t.mainloop()