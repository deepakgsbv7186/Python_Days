# function to take right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# initial steps
put()
turn_left()
turn_left()
move()

# loop until object found
# and check whether
# the conditions
while not object_here():
    if wall_in_front():
        turn_left()
    elif right_is_clear():
        turn_right()
        move()
    elif not wall_on_right():
        turn_right()
    else:
        move()  
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
# from around 1 variable
# this function allows to put some object
put()
# move step forward 
move()
# check the condition and move
# until object found
while not object_here():
    if wall_in_front():
        turn_left()
    else:
        move()
        
        
# from around 1 apple        
def walk_and_collect():  
    for left in range(4):        
        for step in range(9):
            move()
            # when apples found 
            # robot will collect it
            if object_here():
                take()
        turn_left()
walk_and_collect()

# around 3
# initial steps
put()
turn_left()
move()
# function to take right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
# loop until object found
# and check whether
# the conditions
while not object_here():
    if wall_in_front():
        turn_left()
    elif right_is_clear():
        turn_right()
        move()
    elif not wall_on_right():
        turn_right()
    else:
        move()  