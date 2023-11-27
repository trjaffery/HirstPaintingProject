import turtle
import random

# import colorgram
# colors = colorgram.extract('image.jpg', 20)
# colors_list = []
# index = 0
#
# for _ in colors:
#     color = colors[index]
#     rgb = color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     rgb_tuple = (r, g, b)
#     colors_list.append(rgb_tuple)
#     index += 1
#

color_list = [(224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105),
              (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44),
              (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31)]

tim = turtle.Turtle()

turtle.colormode(255)
tim.shape("turtle")
tim.hideturtle()
tim.penup()

tim.setx(-250)
tim.sety(-250)

tim.speed(0)


def make_row():
    for _ in range(9):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.dot(20, random.choice(color_list))


def respawn(row):
    tim.setx(-250)
    tim.sety(-250 + (50 * row))


row_num = 0
for _ in range(10):
    respawn(row_num)
    make_row()
    row_num += 1



screen = turtle.Screen()
screen.exitonclick()