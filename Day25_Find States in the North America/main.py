import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. states game")

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
guessed_state = []

for i in range(50):
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess State Correct",
                                    prompt="What's another state's name").title()
    print(answer_state)

    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())

screen.exitonclick()