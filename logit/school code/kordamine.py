import random

age = int(input('how old be ye'))
if (age < 0):

newrandom = random.randint(0,age)

awnser = input(f'do you wish to be {newrandom} years older')
newage = age + newrandom

if(awnser.lower() == 'yes'):
    print(f'now you are {age + newrandom} years old')
    if(newage >= 18):
        print('you may be let in')
    elif(newage <= 17):
        print('no ewntwy')

elif(awnser.lower() == 'no'):
    print(f'have fun as a {age} year old')


else:
    print('err not andastand')