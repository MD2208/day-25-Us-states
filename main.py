import pandas
import turtle
from state import State
from score import Score
my_screen = turtle.Screen()
my_screen.setup(width=800,height=600)
IMAGE = "blank_states_img.gif"
my_screen.title("U.S. States Game")
my_screen.addshape(IMAGE)
turtle.shape(IMAGE)
score = Score()
## Get the Data
state_data = pandas.read_csv("50_states.csv")
list_of_states = state_data['state'].to_list()
guessed_states = []
missing_states = []
is_game_on = True

while is_game_on:
    if score.score==0:
        answer = my_screen.textinput(title="Guess the State", prompt="What's another state's name?")
    else:
        answer = my_screen.textinput(title=f"{score.score}/50 states", prompt="What's another state's name?")
    answer=answer.lower().title()

    if answer in list_of_states:
        x_cor= int(state_data[state_data['state']==answer]["x"].to_list()[0])
        y_cor= int(state_data[state_data['state']==answer]["y"].to_list()[0])
        new_state = State()
        new_state.create(x_cor,y_cor,answer)
        score.increment_score() 
        guessed_states.append(answer)
    
    if score.score >= 50:
        is_game_on = False
    if answer.lower() == "exit":
        for state in list_of_states:
            if state not in guessed_states:
                missing_states.append(state)
        # if we want to record missing states as in csv file as a data frame ...
        # new_data = pandas.DataFrame(missing_states)
        # new_data.to_csv("states_to_learn.csv")
        is_game_on = False

