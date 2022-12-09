import pandas
from turtle import Turtle, Screen

data = pandas.read_csv("50_states.csv")
# print(data[data.state == "Alabama"])


screen = Screen()
background = Turtle()
mr_text = Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
background.shape(image)
data_states_len = len(data.state)

mr_text.penup()
mr_text.hideturtle()
mr_text.color("black")
game_on = True
score = 0
states_to_learn = data.state.to_list()

while game_on:
    answer_state = screen.textinput(title=f"{score}/{data_states_len}", prompt="What's another state's name?\nTo give "
                                                                               "up enter Y")
    capital_answer = answer_state.capitalize()

    for i in data.state:
        # To find the guessed state coordinates
        if i == capital_answer:
            state_cor = data[data.state == capital_answer]
            mr_text.goto(int(state_cor.x), int(state_cor.y))
            mr_text.write(capital_answer, align="center", font=("Arial", 10, "normal"))
            score += 1
            states_to_learn.remove(capital_answer)
        elif capital_answer == "Y":
            game_on = False
            learn_states = {
                "states": states_to_learn
            }
            datas = pandas.DataFrame(learn_states)
            datas.to_csv("states to learn.csv")

        elif score == data_states_len:
            mr_text.goto(0, 0)
            mr_text.write("Congratulations you've guessed all states!", align="center", font=("Arial", 20, "normal"))
            game_on = False
