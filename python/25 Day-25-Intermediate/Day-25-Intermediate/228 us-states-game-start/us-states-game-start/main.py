import turtle 
import pandas as pd

screen = turtle.Screen()
screen.title("ethiopian map")

screen.addshape("image.gif")

turtle.shape("image.gif")
data = pd.read_csv("coordinates.csv")
def get_mouse(x, y):
    print(x, y)
    

all_city = []
guess_city = []

game_is_active = 16
score = 0
while game_is_active:
    game_is_active -= 1
    answer = screen.textinput(title=f"{score}/16", prompt="Write the name of the city").upper()
    all_city = data["State"] 
    city = data[data["State"]== answer]
    if answer == "EXIT":
        missed_city =[state  for state in all_city if not state in guess_city]
        new_data = pd.DataFrame(missed_city)
        new_data.to_csv("missed_city.csv")
        break 
    if not city.empty:
        guess_city.append(city["State"].item())
        city_y = city["Y"].iloc[0]  
        city_x = city["X"].iloc[0]
        score += 1
        t=turtle.Turtle()
        t.penup()  
        t.goto(x=(city_x/1.5), y=(city_y/2))
        t.color("red")
        t.write(city["State"].item())  

screen.onscreenclick(get_mouse)
screen.mainloop()