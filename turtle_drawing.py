import turtle

def do_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

        
def draw_circle():

    pitt= turtle.Turtle()
    pitt.shape("arrow")
    pitt.color("blue")
    pitt.circle(100)
    pitt.speed(10)

def do_triangle(some_turtle):

    some_turtle.forward(100)
    some_turtle.right(120)
    some_turtle.forward(100)
    some_turtle.right(120)
    some_turtle.forward(100)

def do_art():

    window= turtle.Screen()
    window.bgcolor("red")

    brad= turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(10)

    for i in range(1,37):
        do_triangle(brad)
        brad.right(10)
    brad.width(2)
    brad.right(90)
    brad.forward(300)
    brad.left(180)
    brad.forward(80)
    brad.right(15)
    for i in range(1,45):
        brad.right(2)
        brad.forward(3)
    brad.right(90)
    for i in range(1,45):
        brad.right(2)
        brad.forward(3)
    

    




    window.exitonclick()
    
        
def draw_circle():

    pitt= turtle.Turtle()
    pitt.shape("arrow")
    pitt.color("blue")
    pitt.circle(100)
    pitt.speed(10)

def do_triangle(some_turtle):



    some_turtle.forward(100)
    some_turtle.right(120)
    some_turtle.forward(100)
    some_turtle.right(120)
    some_turtle.forward(100)

do_art()


