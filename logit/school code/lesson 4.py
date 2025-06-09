import random
#gamblin
panus = int(input('bet amount'))
awnser = int(input('what side is facing up'))

if (random.randint(1,6) == awnser):
    print(f'you win u get {panus*5}')
else:
    print(f'you lose, you have lost your {panus} amount of money')
