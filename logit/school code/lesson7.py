
import turtle


age = int(input('how old be ye'))
if (age <= 3):
    print('to young to use this')
    quit()
side = 360 / age
car = turtle.color(input('what be ye fave color'))
if(age >= 24):
    turtle.circle(50)
    

else:
    for i in range(int(age)):
        turtle.fd(side*3)
        turtle.lt(side)


turtle.begin_fill()
turtle.end_fill()


turtle.exitonclick()