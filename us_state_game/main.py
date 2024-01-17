import turtle
import pandas



screen = turtle.Screen()
screen.title("US state Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_state = data["state"].to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_state = [state for state in all_state if state not in guessed_state]
        # for state in all_state:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        new_df = pandas.DataFrame(missing_state)
        new_df.to_csv("states_to_learn.csv")
        break
    
    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"]==answer_state]
        x_coord = int(state_data["x"])
        y_coord =  int(state_data["y"])
        t.goto(x_coord, y_coord)
        t.write(answer_state)



        
