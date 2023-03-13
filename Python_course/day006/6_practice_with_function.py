#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_straight():
    while wall_in_front() != True and at_goal() != True:
        move()


def move_up():
    turn_left()
    while right_is_clear() != True and at_goal() != True:
        move()


def move_right():
    turn_right()
    move()
    turn_right()


def move_down():
    while front_is_clear():
        if not at_goal():
            move()
    turn_left()


while not at_goal():
    move_straight()
    if not at_goal():
        move_up()
    move_right()
    if not at_goal():
        move_down()
