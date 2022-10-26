import random

choose = input('Pick a number 1/10 ')
botnum = random.randint(1,10)

if botnum == choose:
    print('You win number: ', choose)
else:
    print('Bot wins number: ', botnum)
