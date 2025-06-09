from turtle import *
from random import randint

username = ''
while (username == ''):
    username = input('pwese entaw name')
arv = int(input('pick a random number (1-20)'))
randomnum = randint(1,20)
begin_fill()
if(arv == randomnum):
    color("black")
    for i in range(4):
        fd(100)
        lt(90)
else:
    def get_coulor(arv):
        match arv:
            case 1|6|11|16:
                color("black")
            case 2|7|12|17:
                color("red")
            case 3|8|13|18:
                color("yellow")
            case 4|9|14|19:
                color('green')
            case 5|10|15|20:
                color('blue')

    def get_shape(arv):
        match arv:
            case 1|2|3|4|5:
                for i in range(2):
                    fd(200)
                    lt(90)
                    fd(100)
                    lt(90)
            case 6|7|8|9|10:
                for i in range(2):
                    fd(100)
                    lt(60)
                    fd(100)
                    lt(120)
            case 11|12|13|14|15:
                for i in range(2):
                    fd(100)
                    lt(60)
                    fd(50)
                    lt(120)
            case 16|17|18|19|20:
                for i in range(1):
                    fd(100)
                    lt(140)
                    fd(130)
                    lt(130)
                    fd(85)
                    lt(90)
    get_coulor(arv)
    get_shape(arv)
    write(username)
end_fill()

exitonclick()

side = 1
while (side < 0):
    side -= 1
    fd(100)