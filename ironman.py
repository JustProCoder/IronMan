from turtle import Turtle, Screen 
from time import sleep

###Top piece
piece1 = [ [0, -2, -3.5, -6.5, -8.5, -8.5, -8.0, -8.5, -7.5, -7.0, -2.0, 0],[0, 0, 7, 5.5, 4, -1, -4, -5.5, -6.5, -5.5, -7.0, -7.0] ]
###Middle piece
piece2 = [ [0, -2.0, -2.5, -5.0, -6.5, -8.8, -9.3, -9.3, -6.0, -5.5, -4.0, -3.2, 0], [-7.5, -7.5, -8.0, -8.3, -8.0, -6.0, -7.5, -8.0, -14.5, -16.5, -17.5, -16.5, -16.5] ]
###Bottom piece
piece3 = [ [0, -3.0, -4.0, -5.5, -6.0, -4.5, -3.0, -1.5, -1.0, 0], [-17.0, -17.0, -18.0, -17.0, -18.5, -20.0, -19.0, -19.0, -18.5, -18.5] ]

t=Turtle()
s=Screen()
t.hideturtle()
s.bgcolor("#ba161e")      #Dark red
s.setup(500, 600)
x_offset, y_offset = 0, 120
zoom_factor = 15
t.speed(2)

def draw_piece(piece):
    t.penup()
    t.goto(piece[0][0] * zoom_factor + x_offset, piece[1][0] * zoom_factor + y_offset)
    t.pendown()
    t.color('#fab104')   #Light Yellow
    t.begin_fill()
    for i in range(1, len(piece[0])):
        x, y = piece[0][i] * zoom_factor + x_offset, piece[1][i] * zoom_factor + y_offset
        t.goto(x, y)
    #color("#f19100")     
    for i in range(len(piece[0])-1, -1, -1):
        x, y = piece[0][i] * zoom_factor * -1 + x_offset, piece[1][i] * zoom_factor + y_offset
        t.goto(x, y)
    t.end_fill()
    

draw_piece(piece1)
draw_piece(piece2)
draw_piece(piece3)
sleep(4)