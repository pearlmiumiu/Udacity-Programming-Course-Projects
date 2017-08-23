import turtle
def draw_square():
	playground=turtle.Screen()

	playground.bgcolor("pink")

	square=turtle.Turtle()
	square.color("green")
	square.shape("turtle")

	square.speed(2)

	steps=4
	step_count=0
	while step_count<steps:
		sqaure.forward(200)
		sqaure.right(90)
		step_count+=1
	playgroud.exitonclick() #clikc any where to exit

draw_square()

