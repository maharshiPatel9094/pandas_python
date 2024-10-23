import turtle
import pandas

# setup the screen object
screen = turtle.Screen()
screen.title("USA states game")

# Load the image
image = r"C:\Users\mahar\Downloads\day-25-us-states-game-start\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the states data
data = pandas.read_csv(r"C:\Users\mahar\Downloads\day-25-us-states-game-start\50_states.csv")
# FIX: Call the to_list() method to get the list of states
all_states = data.state.to_list()  # Corrected to call the method
guessed_states = []

# Game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state's name?").title()
    
    # for exiting the game
    if answer_state == "Exit":
        # get the list of all missing states
        missing_states = [state for state in all_states if state not in guessed_states]
        
        # make a csv of all missing states
        new_data = pandas.DataFrame(missing_states, columns=["states_to_learn"])
        new_data.to_csv(r"C:\Users\mahar\Downloads\day-25-us-states-game-start\missing_states.csv", index=False)
        break
    
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        
        # Get the x and y coordinates of the guessed state
        state_data = data[data.state == answer_state]
        tim.goto(state_data.x.item(), state_data.y.item())
        
        # Write the name of the state at its location
        tim.write(answer_state)

# Exit on click
# screen.exitonclick()
