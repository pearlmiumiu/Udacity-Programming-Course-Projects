import turtle

def draw_art1():
	playground=turtle.Screen()

	playground.bgcolor("pink")

	angie=turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")

	angie.speed(10)
	for i in range(1,37):
		angie.circle(100)
		angie.right(10)
	window.exitonclick()

#draw_art1()

def draw_rhombus(some_turtle):

	for i in range(1,3):
		some_turtle.forward(100)
		some_turtle.left(45)
		some_turtle.forward(100)
		some_turtle.left(135)


def draw_art2():
	playground=turtle.Screen()

	playground.bgcolor("pink")

	#create the turtle rhombus
	rhombus=turtle.Turtle()
	rhombus.shape("turtle")
	rhombus.color("green")
	rhombus.speed(5)

	for i in range(1,37):
		draw_rhombus(rhombus)
		rhombus.right(10)
	window.exitonclick()
    
draw_art2()



