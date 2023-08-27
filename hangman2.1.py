def open_wordlist():
    global lst
    lst = []
    
    file = 'wordlist.txt'
    fhand= open(file)
    

    for lines in fhand:
        words = lines.split()
        for word in words:
            lst.append(word)

def The_word():
    global letters
    letters = []
    global points
    points = 0
    import random

    index = random.randint(0,len(lst)-1)
    word = str(lst[index])
    for items in word:
        temp = items.split()
        for alphabet in temp:

            letters.append(alphabet)

    letters.pop()
    global hint1, hint2, hint3,hints
    hint1 = "HERE'S A HINT - WORD STARTS WITH: " + letters[0].upper()
    hint2 = "HERE'S A HINT - SECOND LETTER IS: " + letters[1].upper()
    if len(letters)>2:
        hint3 = "HERE'S A HINT - THIRD LETTER IS: " + letters[2].upper()
    hints = [hint1,hint2,hint3]
import turtle 
h = turtle.Turtle()
    
def create_hang():
    h.goto(0,50)

    h.goto(-150,50)

    h.goto(-150,-200)

    h.goto(-120,-200)

    h.goto(-180,-200)

    h.goto(-150,-200)

    h.goto(-150,-10)
    
    h.goto(-100,50)

    h.penup()

    h.home()

    h.pendown()

def head():
    h.circle(-20)

    h.penup()

    h.goto(0,-40)

    h.pendown()

def body():
    h.goto(0,-100)

def leg1():
    h.goto(-30,-140)

    h.goto(0,-100)

def leg2():
    h.goto(30,-140)

    h.penup()

    h.goto(0,-40)

def arm1():
    h.pendown()

    h.goto(-30,-80)

    h.goto(0,-40)

def arm2():
    h.goto(30,-80)

    h.penup()

def reset():
    h.reset()
    h.pendown()


import score

global player
player = score.points()
player.saved_score()
def Game_start():
    import random
    import os
    clear = lambda: os.system('cls')
    
    
    open_wordlist()
    
    The_word()

    index_dic = dict()
    keys = 0
    place = 0
    
    for letter in letters:
        keys = keys + 1
        index_dic[keys]= "__"
        
    correct_word= dict()
    
    for letter in letters:
        place = place + 1
        correct_word[place]= letter
    for a,b in index_dic.items():
        print(b.upper(),end=' ')
    print('\n')
    chances = 6
    create_hang()
    hd = 0
    bdy = 0
    l1 = 0
    l2 = 0
    a1 = 0
    while correct_word != index_dic:
        place = 0
        userinp = input('\nENTER A LETTER:')
        clear()
        print('')
        user = userinp.lower()
        try:
            x = int(user)
            print('Invalid Input')
            continue
        except:
            pass
        if user.lower() == 'quit':
            break
        if len(user) > 1 :
            print('Invalid Input')
            continue
        if user in letters:

            for letter in letters:
                if user == letter:
                    place = place + 1
                    index_dic[place]=user


                else:
                    place = place+1
        if user not in letters:
            chances = chances-1
            print(f'Letter "{user.upper()}" is not in the word')
            print(f'\nYou have "{chances}" chances remaining\n')
        if chances == 0:
            
            print('YOUR WORD WAS:',end =' ')
            for letter in letters:
                print(letter.upper(), end = " ")
            arm2()
            print('\n    ***GAME OVER!***\n')
            player.lose()
            a=1
            while a==1:
                play_again = input('\nDo You want to play again?y/n: ')
                if play_again.lower() == 'y':
                    reset()
                    Game_start()
                    a=0
                elif play_again.lower() == 'n':
                    
                    while True:
                        save = input('\nDo you want to save score?y/n:')
                        if save == 'y':
                            turtle.bye()
                            break
                        elif save == 'n':
                            player.reset_score()
                            turtle.bye()
                            break
                        else:
                            print('Invalid Input')
                    break
                else:
                    print('Invalid Input')
            break


        for a,b in index_dic.items():
            print(b.upper(),end=' ')
        print('\n')

        if chances == 5 and hd==0 :
            head()
            hd=1
            
        elif chances == 4 and bdy==0:
            body()
            bdy=1
            if len(letters)>6:
                abx = random.randint(0,len(hints)-1)
                print(hints[abx])
                hints.remove(hints[abx])
                
        elif chances == 3 and l1 == 0:
            leg1()
            l1 = 1
            if len(letters)>4:
                aby = random.randint(0,len(hints)-1)
                print(hints[aby])
                hints.remove(hints[aby])
        elif chances == 2 and l2 == 0:
            l2 = 1
            leg2()
            if len(letters)>3:
                abz = random.randint(0,len(hints)-1)
                print(hints[abz])
                hints.remove(hints[abz])
        elif chances == 1 and a1 == 0:
            arm1()
            a1 =1
        if correct_word == index_dic:
            print('   ***YOU WIN!***\n')

            player.win()
            a=1
            while a==1:
                play_again = input('\nDo You want to play again?y/n: ')
                if play_again.lower() == 'y':
                    reset()
                    Game_start()
                    a=0
                elif play_again.lower() == 'n':
                    
                    while True:
                        save = input('\nDo you want to save score?y/n:')
                        if save == 'y':
                            turtle.bye()
                            break
                        elif save == 'n':
                            player.reset_score()
                            turtle.bye()
                            break
                        else:
                            print('Invalid Input')
                            continue
                    break
                else:
                    print('Invalid Input')
            break

            
Game_start()