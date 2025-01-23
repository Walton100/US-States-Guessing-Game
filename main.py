from turtle import Turtle,Screen
import pandas
turtle=Turtle()
writer=Turtle()
writer.hideturtle()
writer.penup()


screen=Screen()
screen.setup(730,510)
screen.title('US States game')
image='usa.gif'
screen.addshape(image)
turtle.shape(image)



data=pandas.read_csv('50_states.csv')

states=data.state.to_list()


game_is_on=True

state_count=0
while game_is_on:


    user_input=screen.textinput(title=f'{state_count}/50 States ',prompt='Guess the 50 states').title()


    if user_input=='Exit':
        game_is_on=False
    if user_input in states:
        states.remove(user_input)

        x=data[data.state==user_input].x.item()
        y=data[data.state==user_input].y.item()

        writer.goto(x,y)

        writer.write(f'{user_input}',font=('Times New Roman',10,'normal'))
        state_count+=1




states_to_learn=pandas.DataFrame(states)
states_to_learn.to_csv('States To Learn.csv')