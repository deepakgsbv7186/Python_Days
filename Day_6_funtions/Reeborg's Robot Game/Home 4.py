def turn_right():
    turn_left()
    turn_left()
    turn_left()
def three_steps():
    move()
    move()
    move()
def L_shape():
    three_steps()  
    turn_left()
    three_steps()
def next_L():
    turn_right()
    move()
    turn_right()
for walk in range(3):
    L_shape()
    next_L()
L_shape()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
