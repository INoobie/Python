import random
def play():
    choice = input('Rock Paper Scissors ')

    choicesforbot = 'Rock', 'Paper', 'Scissors'

    botchoice = random.choice(choicesforbot)

    botwin = False
    playerwin = False

    if choice == 'Rock' and botchoice == 'Paper':
        botwin = True
    elif choice == 'Paper' and botchoice == 'Scissors':
        botwin = True
    elif choice == 'Scissors' and botchoice == 'Rock':
        botwin = True
    elif botchoice == 'Rock' and choice == 'Paper':
        playerwin = True
    elif botchoice == 'Paper' and choice == 'Scissors':
        playerwin = True
    elif botchoice == 'Scissors' and choice == 'Rock':
        playerwin = True

    if botwin == True:
        print('Bot wins!')
    elif playerwin == True:
        print('Player wins!')
play()
while True:
    retry = input('want to play again (y/n)')
    if retry == 'y':
        play()
