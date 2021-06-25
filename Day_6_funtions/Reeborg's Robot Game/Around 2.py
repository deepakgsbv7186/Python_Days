put()
move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not object_here():
    if front_is_clear():
        move()
    if not wall_on_right():
        turn_right()
    if wall_in_front():
        turn_left()
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