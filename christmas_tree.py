import turtle as turt

screen = turt.Screen()
screen.bgcolor("sky blue")
screen.title("Christmas Tree")

tree = turt.Turtle()
tree.speed(2)

tree.color("saddle brown")
tree.begin_fill()
tree.penup()
tree.goto(-15, -100)
tree.pendown()
for _ in range(2):
    tree.forward(30)
    tree.left(90)
    tree.forward(40)
    tree.left(90)
tree.end_fill()

def draw_triangle(color, width, height):
    tree.color(color)
    tree.begin_fill()
    tree.forward(width)
    tree.left(120)
    tree.forward(height)
    tree.left(120)
    tree.forward(width)
    tree.left(120)
    tree.end_fill()

tree.penup()
tree.goto(-50, -60)
tree.pendown()
draw_triangle("green", 100, 100)

tree.penup()
tree.goto(-40, -30)
tree.pendown()
draw_triangle("green", 80, 80)

tree.penup()
tree.goto(-30, 0)
tree.pendown()
draw_triangle("green", 60, 60)

tree.color("yellow")
tree.begin_fill()
tree.penup()
tree.goto(-10, 60)
tree.pendown()
for _ in range(5):
    tree.forward(20)
    tree.right(144)
tree.end_fill()

tree.color("red")
tree.penup()
tree.goto(-100, -150)
tree.pendown()
tree.write("Merry Christmas", font=("Arial", 24, "bold"))

tree.hideturtle()

screen.mainloop()
