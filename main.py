import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for x in range(3, 11):
  tim.color(random.choice(colours))
  for y in range(x):
    tim.forward(100)
    tim.right(360/x)

screen = t.Screen()
screen.exitonclick()