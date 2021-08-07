import turtle

# s = turtle.Screen()
# s.setup(1200, 600, 0, 0)
t = turtle.Turtle()
t.speed(10000)
t.ht()


def draw_koch(len_val, turt_le):
    if len_val > 6:
        len_val = len_val // 3
        draw_koch(len_val, turt_le)
        turt_le.left(60)
        draw_koch(len_val, turt_le)
        t.right(120)
        draw_koch(len_val, turt_le)
        turt_le.left(60)
        draw_koch(len_val, turt_le)
    else:
        turt_le.forward(len_val)
        turt_le.left(60)
        turt_le.forward(len_val)
        t.right(120)
        turt_le.forward(len_val)
        turt_le.left(60)
        turt_le.forward(len_val)


draw_koch(150, t)
t.right(120)
draw_koch(150, t)
t.right(120)
draw_koch(150, t)
t.left(90)
t.forward(5)
draw_koch(150, t)
t.right(120)
draw_koch(150, t)
t.right(120)
draw_koch(150, t)
turtle.done()
