import turtle
import pandas


correct_ans = 0
screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state = turtle.Turtle()

data = pandas.read_csv("50_states.csv")
data_list = data["state"].to_list()

while correct_ans != 50:
    answer_state = screen.textinput(title=f"{correct_ans}/50 answers correct", prompt="What`s another states name?")
    if answer_state == "exit":
        states_to_learn = data_list
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    for _ in data_list:
        if _ == answer_state:
            x_coord = int(data[data.state == answer_state].x)
            y_coord = int(data[data.state == answer_state].y)

            state.penup()
            state.goto(x_coord, y_coord)
            state.hideturtle()
            state.write(f"{answer_state}", align="center", font=("Courier", 8, "normal"))
            correct_ans += 1
            data_list.remove(_)
        else:
            continue
