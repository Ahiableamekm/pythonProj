def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def jump_wall():
    if wall_on_right():
        move()
    else:
        turn_right()
        move()
            
while not at_goal():
    if not right_is_clear():
        turn_left()
    else:
        jump_wall()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
