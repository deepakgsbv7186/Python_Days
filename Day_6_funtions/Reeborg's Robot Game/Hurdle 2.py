def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# until the flag not found
# robot will cross hurdle
found = 1
while found:
    jump()
    if at_goal():
        found = 0
        
# another method shortone
while not at_goal():
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
