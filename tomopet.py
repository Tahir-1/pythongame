import random as ran
import time as ti
import sys 

start = input('Do you want a pet? \n enter y to start: ')
petlist = ['dog','cat','rabbit']
petattribute = {'dog':'frendly','cat':'sleepy','rabbit':'energetic'}
nick = ''

def game():
    print(' 1. to flip coin \n 2. rock paper sissors \n 3.tic tac toe ')
    gameind = int(input('Enter no. what yoou want to play?'))
    if gameind == 1 :
        coin = int(input('choose \n 1. for heads \n 2.for tail'))
        won = ran.randint(1,2)
        if won == 1:
            print('its heads')
        else:
            print('its tails')
        if coin == won:
            print(' you win')
        else:
            print('You lose')
    if gameind == 2:
        play = int(input('choose \n 1. for rock \n 2.for paper \n 3.for sissors'))
        computer = ran.randint(1,3)
        if play == computer :
            print('its a draw')
        elif play == 1 and computer == 2:
            print('its paper \nyou won')
        elif play == 2 and computer == 3:
            print('its sicssors \nyou won')
        elif play == 3 and computer == 1:
            print('its rock \nyou won') 
        else:
            print('you lose')
    if gameind ==3:
        import random
        nonx = []
        nonc = []
        numar = [1,2,3,4,5,6,7,8,9]
        def check():
            for x in range(0,9,3):
                print(numar[x+0],numar[x+1],numar[x+2])
        def win():
            combo = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
            for x in combo:
                if x[0] in nonx and x[1] in nonx and x[2] in nonx:
                    print('you won')
                    return True
                if x[0] in nonc and x[1] in nonc and x[2] in nonc:
                    print('you lose')
                    return True
        check()
        for x in range(5):
            xval = int(input("enter a number "))
            nonx.append(xval)
            numar[xval-1]= 'x'
            rak = random.randint(1,9)
            while ran in nonx:
                rak = random.randint(1,9)
            else:
                numar[rak-1] = 'o'
                nonc.append(rak)
            check()
            if win():
                break    
    ti.sleep(0.5)
        
def chosepet():
    for i in range(0,len(petlist)):
        print(i+1,'.',petlist[i])
    pet = int(input("enter the pet no."))
    print('Your new pet is a',petlist[pet-1])
    nick = input('Give your pet a nickname ')
    ti.sleep(1)
    print(nick ,'is a cute name')
    ti.sleep(1)
    print(nick,' is a',petattribute[petlist[pet-1]]," ",petlist[pet-1])
    def tasks():
        t = 'y'
        hunger = 50
        while(t == 'y'):
            ti.sleep(1)
            print(' 1.feed \n 2.play \n 3.pat \n 4.hug \n 5.exit')
            k = int(input("Enter no. what you want to do?"))
            if k == 1:
                if hunger == 100 :
                    print( nick , ' is full')
                else:
                    hunger = hunger + 10
                    print(nick,' hunger = ', hunger)
            elif k == 2:
                game()
            elif k == 3 or k ==4 :
                print(nick,' is happy')
            else:
                print('Thanks for playing')
                sys.exit() 

    tasks()

def startgame():
    chosepet()
    

if start == 'y':
    startgame()
else:
    print('thanks for checking out')
