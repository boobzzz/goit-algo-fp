import turtle
import math


def draw_fractal(branch_length, angle, level):
    if level == 0:
        turtle.forward(branch_length)
        turtle.backward(branch_length)
        return

    turtle.forward(branch_length)

    turtle.left(angle)
    draw_fractal(branch_length * math.cos(math.radians(angle)), angle, level - 1)

    turtle.right(2 * angle)

    draw_fractal(branch_length * math.cos(math.radians(angle)), angle, level - 1)

    turtle.left(angle)
    turtle.backward(branch_length)


level = int(input("Введіть рівень рекурсії: "))
turtle.speed(0)
turtle.left(90)
turtle.up()
turtle.backward(200)
turtle.down()
draw_fractal(100, 45, level)
turtle.done()
