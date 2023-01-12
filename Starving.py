
P2 = 'computer'
print('Welcome!')
import time, sys, random

#constant variables
boardwidth = 10
boardheight = 10
letterline= ' | A | B | C | D | E | F | G | H | I | J |'
boards = []
boat = '[ ]'
hitboat = '[X]'
miss = ' X '
trueend = False
new = True
surrender = False
hitcomment = ['You are the greatest player I\'ve ever seen!!', 'You are Rocking it!', 'YEEEEAAAAHHHHH!!','Wow! Such a great shot!', 'LET\'S GOOOOOOOO!!']
misscomment =['HAHAHAHAHAHAHAHAHAHA!!','...Really?','Oh,oh,oh, how can anyone play so badly...', 'Captain, I am truly disappointed in you...', 'AGAIN?!!', 'You better get it next time...!!']
welcomecomment =['It is an honor to let you play, ', 'Be our guest, ', 'Welcome aboard, ']
sunkstate1 = ['','','','']
sunkstate2 = ['','','','']
setdirection = ''
chosendirection = ''

#prints letter by letter
def sprint(str):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(7./170)

#prints bunch of space
def space():
    print('\n'*50)

#creating empty boards
def emptyboard():
    for i in range(0,4):
        grid = []
        for k in range(boardwidth):
            line = []
            line.append(k)
            for j in range(boardwidth):
                line.extend(['|','   '])
            line.append('|')
            grid.append(line)
        boards.append(grid)

#creates empty board
emptyboard()


#states boards
P1Board = boards[0]
P1AttackBoard = boards[1]
P2Board = boards[2]
P2AttackBoard = boards[3]

#printing board
def print_board(board):
    print(letterline)
    for b in board:
        for a in b:
            print(a,end='')
        print()

#setting up the board with ships
def setupboard(board):
    sunkstate = []
    if board == P1Board:
        sunkstate = sunkstate1
    elif board == P2Board:
        sunkstate = sunkstate2
    print_board(board)
    availableboat = [2, 3, 4, 5]
    x = True
    while x == True:
        userinput1 = input("??: ")
        userinput2 = input('??: ')

        #check if the input has more or less letters than 2
        if len(userinput1) != 2 or len(userinput2) != 2:
            sprint("Invalid: Code#0 - Your input has to have only one letter and one number")
            print_board(board)
            continue
        if userinput1[1].isdigit() == False or userinput2[1].isdigit() == False:
            sprint("Invalid: Code#1 - Your input has to have a number for second place in a input. i.e. A\'7\' or F\'3\'.")
            print_board(board)
            continue
        #set up the variables(divide the inputs into first letters and second letters)
        inputline1 = int(ord(userinput1[0])) -65
        column1 = userinput1[1]
        inputline2 = int(ord(userinput2[0])) - 65
        column2 = userinput2[1]

        #check if the input is valid under various circumstances
        if inputline1 != inputline2 and column2 != column1:
            sprint("Invalid: Code#2 - One of your letters or numbers have to be the same. i.e. A5,A6 or A5,B5")
            print_board(board)
            continue
        if inputline1 > 10 or inputline2 > 10 or inputline1 < 0 or inputline2 < 0:
            sprint("Invalid: Code#3 - The letter have to be between 'CAPITALIZED LETTER' 'A to J'")
            print_board(board)
            continue
        if max(inputline1,inputline2) - min(inputline1,inputline2) > 4 or max(int(column1),int(column2)) - min(int(column1),int(column2)) > 4:
            sprint("Invalid: Code#4 - The maximum length of the ship is 5. i.e. A2,A8 or A4,H4 are invalid.")
            print_board(board)
            continue

        #if passed all tests, put in the coordinate of the boat
        else:
            #identify what line it is from the first and second input
            theline1 = board[int(column1)]

            #check if first letters of both input are same(i.e. A3, A5)
            if inputline1 == inputline2:
                #checks if length of ship is used already
                length = int(max(column1,column2)) - (int(min(column1,column2)))+1
                if length in availableboat:

                    #check if the ships overlap
                    checkok = False
                    for i in range(min(int(column1),int(column2)),max(int(column2),int(column1))+1):
                        theline = board[i]
                        if theline[2 * inputline1 + 2] == '[ ]':
                            sprint("Invalid: Code#5 - The ships may not overlap")
                            checkok = False
                            break
                        else:
                            checkok = True
                            continue

                    sunk = []
                    #change the items in the list to the boat
                    if checkok == True:
                        for i in range(min(int(column1),int(column2)),max(int(column2),int(column1))+1):
                            sunk.append(i)
                            theline = board[i]
                            theline[2 * inputline1 + 2] = boat
                        #saving coordinates of the boats with each length to check if they are sunk
                        sunkcoord = []
                        for i in sunk:
                            sunkcoord.append(str(chr(inputline1+65))+str(i))
                        sunkstate[(length-2)] = sunkcoord
                        availableboat.remove(length)
                else:
                    sprint("Invalid: Code#6 - There cannot be more than 1 ship with same length. The available lengths of ships are: "+str(availableboat))

            # check if second letters of both input are same(i.e. A3, C3)
            if column1 == column2:
                # check if length is already used
                length = max(inputline1, inputline2) - min(inputline1, inputline2) + 1
                if length in availableboat:
                    # check if the ships overlap
                    checkok = False
                    for i in range(min(inputline1, inputline2), max(inputline1, inputline2) + 1):
                        if theline1[2 * i + 2] == '[ ]':
                            sprint("Invalid: Code#5 - The ships may not overlap")
                            checkok = False
                            break
                        else:
                            checkok = True
                            continue

                    sunk = []
                    # change the items in the list to the boat
                    if checkok == True:
                        for i in range(min(inputline1, inputline2), max(inputline1, inputline2) + 1):
                            sunk.append(chr(int(i)+65))
                            theline1[2 * i + 2] = boat
                        #saving coordinates of the boats with each length to check if they are sunk
                        sunkcoord = []
                        for i in sunk:
                            sunkcoord.append(str(i)+str(column1))
                        sunkstate[length-2] = sunkcoord
                        availableboat.remove(length)
                else:
                    sprint("Invalid: Code#6 - There cannot be more than 1 ship with same length. The available lengths of ships are: " + str(availableboat))

            # if ships are all set up, break out of the loop
            if len(availableboat) == 0:
                print_board(board)
                sprint("You are all set up!")
                time.sleep(3)
                return ''

        print_board(board)

def comsetupboard(board):
    sunkstate = []
    if board == P1Board:
        sunkstate = sunkstate1
    elif board == P2Board:
        sunkstate = sunkstate2
    availableboat = [2, 3, 4, 5]
    x= True
    while x == True:
        inputline1 = random.randint(0,9)
        column1 = random.randint(0,9)
        inputline2 = random.randint(0,9)
        column2 = random.randint(0,9)
        if inputline1 != inputline2 and column2 != column1:
            continue
        if inputline1 > 10 or inputline2 > 10 or inputline1 < 0 or inputline2 < 0:
            continue
        if max(inputline1,inputline2) - min(inputline1,inputline2) > 4 or max(int(column1),int(column2)) - min(int(column1),int(column2)) > 4:
            continue
            # if passed all tests, put in the coordinate of the boat
        else:
            # identify what line it is from the first and second input
            theline1 = board[int(column1)]
            # check if first letters of both input are same(i.e. A3, A5)
            if inputline1 == inputline2:
                # checks if length of ship is used already
                length = int(max(column1, column2)) - (int(min(column1, column2))) + 1
                if length in availableboat:
                    # check if the ships overlap
                    checkok = False
                    for i in range(min(int(column1), int(column2)), max(int(column2), int(column1)) + 1):
                        theline = board[i]
                        if theline[2 * inputline1 + 2] == '[ ]':
                            checkok = False
                            break
                        else:
                            checkok = True
                            continue

                    sunk = []
                    # change the items in the list to the boat
                    if checkok == True:
                        for i in range(min(int(column1), int(column2)), max(int(column2), int(column1)) + 1):
                            sunk.append(i)
                            theline = board[i]
                            theline[2 * inputline1 + 2] = boat
                        # saving coordinates of the boats with each length to check if they are sunk
                        sunkcoord = []
                        for i in sunk:
                            sunkcoord.append(str(chr(inputline1 + 65)) + str(i))
                        sunkstate[(length - 2)] = sunkcoord
                        availableboat.remove(length)
            # check if second letters of both input are same(i.e. A3, C3)
            if column1 == column2:
                # check if length is already used
                length = max(inputline1, inputline2) - min(inputline1, inputline2) + 1
                if length in availableboat:
                    # check if the ships overlap
                    checkok = False
                    for i in range(min(inputline1, inputline2), max(inputline1, inputline2) + 1):
                        if theline1[2 * i + 2] == '[ ]':
                            checkok = False
                            break
                        else:
                            checkok = True
                            continue
                    sunk = []
                    # change the items in the list to the boat
                    if checkok == True:
                        for i in range(min(inputline1, inputline2), max(inputline1, inputline2) + 1):
                            sunk.append(chr(int(i) + 65))
                            theline1[2 * i + 2] = boat
                        # saving coordinates of the boats with each length to check if they are sunk
                        sunkcoord = []
                        for i in sunk:
                            sunkcoord.append(str(i) + str(column1))
                        sunkstate[length - 2] = sunkcoord
                        availableboat.remove(length)
            if len(availableboat) == 0:
                print_board(board)
                sprint("Computer is all set up!")
                time.sleep(3)
                return ''

#attacking stage of the game
def attackboard(board):
    print_board(board)
    infoboard = []
    ownboard = []
    sunkstate = []
    #setting up the boards depending on who is playing at the moment
    if board == P1AttackBoard:
        infoboard = P2Board
        ownboard = P1Board
        sunkstate = sunkstate2
    elif board == P2AttackBoard:
        infoboard = P1Board
        ownboard = P2Board
        sunkstate = sunkstate1
    x = True
    while x == True:
        fire = input("??: ")
        #check if the player wants to take a look at his/her board
        if fire == 'board':
            space()
            sprint('Here is your board for the reference.')
            print_board(ownboard)
            input('When you are ready, enter anything to go back to attack board:')
            space()
            print_board(board)
            continue
        if fire == 'surrender':
            sprint('Wow... I never thought there would be such a lame player to surrender...')
            sprint('Still, if that is what you want, I will let you surrender.')
            time.sleep(2)
            global surrender
            surrender = True
            break
        # check if the input has more or less letters than 2
        if len(fire) != 2:
            sprint("Invalid: Code#0 - Your input has to have only one letter and one number")
            print_board(board)
            continue
        # check if the letter on the second place is a number
        if fire[1].isdigit()==False:
            sprint("Invalid: Code#1 - Your input has to have a number for second place in a input. i.e. A\'7\' or F\'3\'.")
            print_board(board)
            continue

        # set up the variables(divide the inputs into first letters and second letters)
        inputline = int(ord(fire[0])) - 65
        column = fire[1]
        # check if the input is valid under various circumstances
        if inputline > 9 or inputline < 0:
            sprint("Invalid: Code#3 - The letter have to be 'CAPITALIZED LETTER' between 'A to J'")


        else:
            # check if the player's guess is hit
            theline = board[int(column)]
            if infoboard[int(column)][2*(inputline)+2] == boat:
                #change the attackboard
                theline[2*(inputline)+2] = hitboat
                #change the original board too
                infoboard[int(column)][2*(inputline)+2] = hitboat
                print_board(board)
                sprint("HITTTTTTTTTTT!!!!!")

                #checks if the boat is sunk!
                for i in sunkstate:
                    maybesunk = 0
                    for j in i:
                        sunkcoord1 = ord(j[0])-65
                        sunkcoord2 = int(j[1])
                        if board[sunkcoord2][2*sunkcoord1+2] == hitboat:
                            maybesunk += 1
                        if maybesunk == len(i):
                            sprint("AANNNDDDD SSSSUUUUUNNNNKKKKKKKK!")
                            i.clear()
                #hit comment
                sprint(random.choice(hitcomment))

                break
            #check if the player already guessed the coordinate
            elif board[int(column)][2*(inputline)+2] == hitboat or board[int(column)][2*(inputline)+2] == miss:
                sprint('Invalid: Code#7 - You already guessed that coordinate...')
            # check if the player's guess is miss
            else:
                #change the attackboard
                theline[2 * (inputline) + 2] = miss
                #change the original board too
                infoboard[int(column)][2 * (inputline) + 2] = miss
                print_board(board)
                sprint("MISSSSSSSS!!!!!")
                sprint(random.choice(misscomment))
                break
        print_board(board)

def comattackboard(board):
    direction = ['up', 'down', 'right', 'left']
    global rootline
    global rootcolumn
    infoboard = []
    sunkstate = []
    # setting up the boards depending on who is playing at the moment
    if board == P1AttackBoard:
        infoboard = P2Board
        sunkstate = sunkstate2
    elif board == P2AttackBoard:
        infoboard = P1Board
        sunkstate = sunkstate1
    x = True
    while x == True:
        global chosendirection, setdirection
        if setdirection == '':
            if rootline and rootcolumn != '':
                if rootline == 0:
                    direction.remove('left')
                if rootline == 9:
                    direction.remove('right')
                if rootcolumn == 0:
                    direction.remove('up')
                if rootcolumn == 9:
                    direction.remove('down')
                chosendirection = random.choice(direction)
                if chosendirection == 'up':
                    column = rootcolumn - 1
                    inputline = rootline
                if chosendirection == 'down':
                    column = rootcolumn + 1
                    inputline = rootline
                if chosendirection == 'right':
                    inputline = rootline + 1
                    column = rootcolumn
                if chosendirection == 'left':
                    inputline = rootline - 1
                    column = rootcolumn
            else:
                inputline = random.randint(0,9)
                column = random.randint(0,9)
        else:
            if setdirection == 'up':
                column = rootcolumn - 1
                inputline = rootline
            if setdirection == 'down':
                column = rootcolumn + 1
                inputline = rootline
            if setdirection == 'right':
                inputline = rootline + 1
                column = rootcolumn
            if setdirection == 'left':
                inputline = rootline - 1
                column = rootcolumn
        theline = board[int(column)]
        if infoboard[int(column)][2 * (inputline) + 2] == boat:
            # change the attackboard
            theline[2 * (inputline) + 2] = hitboat
            # change the original board too
            infoboard[int(column)][2 * (inputline) + 2] = hitboat
            print_board(board)
            sprint("HITTTTTTTTTTT!!!!!")
            setdirection = chosendirection
            rootline = inputline
            rootcolumn = column

            # checks if the boat is sunk!
            for i in sunkstate:
                maybesunk = 0
                for j in i:
                    sunkcoord1 = ord(j[0]) - 65
                    sunkcoord2 = int(j[1])
                    if board[sunkcoord2][2 * sunkcoord1 + 2] == hitboat:
                        maybesunk += 1
                    if maybesunk == len(i):
                        sprint("AANNNDDDD SSSSUUUUUNNNNKKKKKKKK!")
                        rootline = ''
                        rootcolumn = ''
                        setdirection = ''
                        i.clear()
            # hit comment
            sprint(random.choice(hitcomment))

            break
        # check if the player already guessed the coordinate
        elif board[int(column)][2 * (inputline) + 2] == hitboat or board[int(column)][2 * (inputline) + 2] == miss:
            continue
        # check if the player's guess is miss
        else:
            # change the attackboard
            theline[2 * (inputline) + 2] = miss
            # change the original board too
            infoboard[int(column)][2 * (inputline) + 2] = miss
            print_board(board)
            sprint("MISSSSSSSS!!!!!")
            sprint(random.choice(misscomment))
            break

        print_board(board)

#ending and redo
def redo(winner):
    space()
    sprint("Congratulation, "+winner+"! You have won the battle!")
    #shows P1 board
    sprint('This was '+P1+'\'s board.')
    print_board(P1Board)
    time.sleep(3)
    #shows P2 board
    sprint('This was '+P2+'\'s board.')
    print_board(P2Board)
    time.sleep(3)
    sprint("Thank you for playing Battleship, "+P1+" and "+P2+"!")
    last = False
    while last == False:
        #ask if player wants to play again
        again = input("Do you wish to play again?(y/n): ")

        if again == 'y':
            sprint('Why not? Let\'s start from the beginning.')
            space()
            global new
            new = False
            last = True

        elif again == 'n':
            sprint('Okay, Bye! Thank you for playing Battleship! :)')
            global trueend
            trueend = True
            last = True
            global end
            end = True
            time.sleep(3)

        else:
            sprint('Invalid: Code#8 - Please only enter \'y\' or \'n\' please...')

    return ''


#Game Play
end = False
while end == False:
    print('Hello! Welcome to BATTLESHIP!!!!!!!!')
    P1 = input('May I ask for the player\'s username?: ')
    sprint(random.choice(welcomecomment)+P1+'!')
    # Game Set up
    print(P1 + "\'s turn to set up.")
    setupboard(P1Board)
    print('Now computer will set the board.')
    time.sleep(2)
    comsetupboard(P2Board)
    rootline = ''
    rootcolumn = ''
    right = False
    while right == False:

        print(P1+"\'s turn to attack! FIRE~!")
        print()
        attackboard(P1AttackBoard)
        if surrender == True:
            redo(P2)
            break
        boatspace = 14
        for i in P2Board:
            x = i.count('[X]')
            boatspace -= x
        if boatspace == 0:
            redo(P1)
            break
        space()
        #second player
        print(P2 + "\'s turn to attack! FIRE~!")
        time.sleep(2)
        print()
        comattackboard(P2AttackBoard)
        boatspace = 14
        for i in P1Board:
            x = i.count('[X]')
            boatspace -= x
        if boatspace == 0:
            redo(P2)
            break
        time.sleep(2)
        space()

    #resetting varibles
    surrender = False
    P1Board.clear()
    P1AttackBoard.clear()
    P2Board.clear()
    P2AttackBoard.clear()
    boards.clear()
    emptyboard()
    P1Board = boards[0]
    P1AttackBoard = boards[1]
    P2Board = boards[2]
    P2AttackBoard = boards[3]