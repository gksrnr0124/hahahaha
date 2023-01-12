import sys,time

#defining function that prints letter by letter
def sprint(str):
 for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(7./70)

#same as above, but slower
def sprint_2(str):
 for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(15./50)

#starts the program by receiving name of a player and welcoming him/her
username = input("Enter your name:")
sprint("Hi, "+username+". Welcome to GAMES!")


#defining hangman(game) #for this game, I got some help from internet for some parts like blanks changing to letter
def hangman( str ):
    #creating list of things that are used for hangman
    list=["notebook","pencilcase","computer","friends","cellphones","protractor","blackboard","whiteboard","compass", "backpack", "pencilsharpner",
          "gluestick", "textbooks", "teachers", "students", "essay", "geography", "science", "international", "religion", "memes", "binder", "folders",
          "lunchbox","lunch", "gymnasium", "bookmark", "microscope", "chromebook", "ruler", "crayons", "principal", "office", "detention", "stapler",
          "highlighter", "globe", "documents", "schoolbus", "bulletinboard", "printer", "projector", "playground", "reportcard", "benches", "basketball", "soccer",
          "volleyball","lockers", "library", "bookshelves", "attendance", "homework"]

    #hangman display
    hangmangraphic = [
    '''        +----+
        |    |
             |
             |
             |
             |
             |
       =========''',
    '''        +----+
        |    |
        O    |
             |
             |
             |
             |
       =========''',
    '''        +----+
        |    |
        O    |
        |    |
             |
             |
             |
       =========''',
    '''        +----+
        |    |
        O    |
        |    |
        |    |
             |
             |
       =========''',
    '''        +----+
        |    |
        O    |
       /|    |
        |    |
             |
             |
     =========''',
    '''        +----+
        |    |
        O    |
       /|\   |
        |    |
             |
             |
       =========''',
    '''        +----+
        |    |
        O    |
       /|\   |
        |    |
       /     |
             |
       =========''',
    '''        +----+
        |    |
        O    |
       /|\   |
        |    |
       / \   |
             |
       =========''']

    #getting random word from the list
    def fetchingword(list):
        #choose the random word and it never changes throughout the game #fetches another random word if the game restarts
        theWord = random.choice(list)
        return theWord


    #manage displays(hangman display, wrong letters, correct letters, and the secret word
    def display(HANGMANPICS, wrong, correct, theWord):
        print("--------------------------------------")
        #to display the hangman display, depending on how many wrong letters the player guessed
        print(HANGMANPICS[len(wrong)])

        #printing wrong letters
        #end=''fuction to print each letters beside each other
        print('Wrong Letters:', end=' ')
        for letter in wrong:
            print(letter+", ",end='')
        print()

        #define blanks
        blanks = '_' * len(theWord)

        #replacing the correct letter into the correct blank in blanks
        for i in range(len(theWord)):
            if theWord[i] in correct:
                blanks = blanks[:i] + theWord[i] + blanks[i+1:]
        for letter in blanks:
            print(letter, end=' ')
        print()

    #this is to store guesses and return the letters that the player already guessed
    def storeGuess(alreadyGuessed):
        finish = False
        alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        while finish == False:
            #ask question and receive input(guess)
            guess=input("Guess a letter:")
            #checks if player guesses something
            if len(guess) == 0:
                sprint("Please enter something...")
            #checks if guess is more than one letter
            elif len(guess) > 1:
                sprint("I sensed CHEATING... Enter ONE letter at a time...")

            #checks if guess is already guessed
            elif guess in alreadyGuessed:
                sprint("You have already guessed that letter. Try again.")

            #checks if the guess is a letter(one of alphbets or not)
            elif guess not in alphabets:
                sprint("Please enter a LETTER.")

            #checks if the guess is in uppercase
            elif guess == guess.upper():
                sprint("Please enter in LOWERCASE.")

            else:
                return guess




    sprint("Hi, "+username+". Let\'s play HANGMAN")
    sprint("The words are going to be about school stuff.")

    #basic settings
    wrong = ''
    correct = ''
    #define the secret word is the random word from the list
    secretWord = fetchingword(list)

    finish = False
    while finish == False:

        display(hangmangraphic, wrong, correct, secretWord)

        #define the guess as all guesses including wrong and correct
        guess = storeGuess(wrong + correct)
        #check if guessed letter is in the secret word
        if guess in secretWord:
            correct = correct + guess
            allCorrect = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correct:
                    allCorrect = False
                    break

            #check if the secret word is completed
            if allCorrect == True:
                display(hangmangraphic, wrong, correct, secretWord)
                sprint("Congratulation! ")
                #show how many wrong and correct guesses player had
                sprint("After " + str(len(wrong)) + " missed guesses and " + str(len(correct))+ " correct guesses,")
                sprint("The secret word is \'" + secretWord + "\'! You have won! You have saved a man's life!:)")
                finish = True

        #same end but when the player ran out of guess
        else:
            wrong = wrong + guess
            #checking if their are any more guesses left
            if len(wrong) == len(hangmangraphic) - 1:
                display(hangmangraphic, wrong, correct, secretWord)
                sprint("You have run out of guesses!")
                sprint("After " + str(len(wrong)) + " missed guesses and " + str(len(correct)) + " correct guesses, the word was \'" + secretWord + "\'!")
                finish = True

        #redo function #see if player wants to play again or not
        if finish == True:
            realfinish = False
            while realfinish == False:
                redo=input("Do you want to play again? (y/n)")
                redo= str.lower(redo)
                #when player wants to play again, reset the basic setting and loop again
                if redo == "y":
                    wrong = ''
                    correct = ''
                    realfinish = True
                    finish = False
                    secretWord = fetchingword(list)
                #if not, end the loop
                elif redo == "n":
                    sprint("Alright, thanks for using the program.")
                    realfinish = True
                    finish = True
                #preventing the code from breaking by random letters or words
                else:
                    sprint("You can only type either \'y\' or \'n\'...")
                    realfinish = False

#-------------------------------------------------------------------------------------------------------------------
#defining guess the number game
def GuessTheNumber( str ):
    sprint("Welcome to the number game, "+username+"!")
    #discribing how to play the game for those who never played guess the number
    sprint("Now, you are going to guess the number between 1 to 100.")
    sprint("I will tell you if the number is higher or lower, and you will have 10 chances to guess.")

    import random
    #setting the random number between 1 to 100
    number=random.randint(1,100)

    #set guess times
    guessTime = 10
    guessTime = int(guessTime)

    while guessTime > 0:
        finish=False
        while finish == False:
            answer=input("Take a guess!:")


            guessTime = guessTime-1

            try:
                integer = int(answer)

                #chekcs if player entered the measurable number for the code
                if int(answer) > 100:
                    sprint("You have to choose a number between 1 to 100...")
                    finish = False
                if int(answer) < 1:
                    sprint("You have to choose a number between 1 to 100...")
                    finish = False

                #checks if input is larger than number
                if int(answer) > number:
                    sprint("Nice guess, but my number is lower.")
                    sprint("You have "+ str(guessTime) + " guesses left.")
                    sprint("------------------------------")
                    finish = False

                #checks if input is smaller than number
                if int(answer) < number:
                    sprint("Nice guess, but my number is higher.")
                    sprint("You have " + str(guessTime) + " guesses left.")
                    sprint("------------------------------")
                    finish = False

                #remind the player that he/she has only one guess left
                if guessTime == 1:
                    sprint("You better guess well this time!")

                #checks if the player ran out of guess
                if guessTime == 0:
                    sprint("You ran out of guess! The correct number was " + str(number) + "!")
                    #redo system
                    end=False
                    while end == False:
                        redo=input("Do you want to play again? (y/n):")
                        if redo == "y":
                            print("")
                            sprint_2("Okay, " + username + ", restarting program...")
                            sprint_2("Program... in... Progress...")
                            sprint("==============================")
                            sprint("Alright! I am set!")
                            #set up the basic settings again
                            import random
                            number=random.randint(1,100)
                            guessTime = 10
                            end=True
                            finish = False
                        elif redo == "n":
                            sprint("Thank you for using the program, "+username+ "! See ya!")
                            end = True
                            finish = True
                            guessTime = -1
                            break
                        else:
                            sprint("You can only enter \'y\' or \'n\'...")
                            end = False


                #checks if input is corect
                if int(answer) == number:
                    sprint("That is the correct number! Congratulation!")
                    #shows how many gueses the player took to guess the correct number
                    sprint("You guessed the right number in "+ str(10-guessTime) + " guesses!")
                    sprint("==============================")
                    #redo system
                    end=False
                    while end == False:
                        redo=input("Do you want to play again? (y/n):")
                        if redo == "y":
                            print("")
                            sprint_2("Okay, " + username + ", restarting program...")
                            sprint_2("Program... in... Progress...")
                            sprint("==============================")
                            sprint("Alright! I am set!")
                            import random
                            number=random.randint(1,100)
                            guessTime = 10
                            end=True
                            finish = False
                        elif redo == "n":
                            sprint("Thank you for using the program, "+username+ "! See ya!")
                            end = True
                            finish = True
                            guessTime = -1
                            break
                        else:
                            sprint("You can only enter \'y\' or \'n\'...")
                            end = False
            #checks if the player enters something that is not number
            except ValueError:
                sprint("Please enter in numbers")
                sprint("You have "+ str(guessTime) + " guesses left.")
                sprint("------------------------------")
                finish = False

#-------------------------------------------------------------------------------------------------------------------
import random
def GuessTheNumber_Reversed( str ):

    sprint("Hi, " + username + "!")

    sprint("Let me guess your number between 1 to 100")
    sprint("Answer in a, b, or c")
    sprint("a: higher")
    sprint("b: lower")
    sprint("c: yes")
    #basic settings
    answer = ''
    lowest = 0
    highest = 100
    number = random.randint(lowest, highest)


    finish = False
    while finish ==  False:
        sprint("------------------------------")
        while answer != "c":
            answer=input("Is your number " + str(number) + "?:")

            if answer == "a":
                #lowest is number plus 1 because the code wouldn't want to include the guessed number
                lowest = number+1
                #checks if the gap between lowest and highest equals 1, which is cheating #i.e. higher than 42 but smaller than 43 = no number to be guessed...
                if abs((lowest-1) - (highest+1)) == 1:
                    sprint("I guess you are cheating...?")
                    sprint_2("Restarting...")
                    sprint("------------------------------")
                    #back to the beginning with basic settings
                    lowest = 0
                    highest = 100
                    answer = ''
                    number = random.randint(lowest, highest)
                #if not cheated move on, set a new lowest bound
                else:
                    number = random.randint(lowest, highest)
                    finish = False

            #same as a but for highest bound
            elif answer == "b":
                highest = number-1
                if abs((lowest-1) - (highest+1)) == 1:
                    sprint("I guess you are cheating...?")
                    sprint("Restarting...")
                    sprint("------------------------------")
                    lowest = 0
                    highest = 100
                    answer = ''
                    number = random.randint(lowest, highest)
                else:
                    finish = False
                    number = random.randint(lowest, highest)
                    finish = False

            #checks if the number is correct
            elif answer == "c":
                sprint("Horray!")
                sprint("That was a tough game! >u<")
                finish = True

                #redo
                end=False
                while end == False:
                    redo = input("Do you want me to guess your number again? (y/n):")
                    if redo == "y":
                        sprint("Ok, restarting in progress...")
                        sprint_2("Let... me... clear... my brain...")
                        sprint("------------------------------")
                        lowest = 0
                        highest = 100
                        answer = ''
                        end = True
                        finish = False
                    elif redo == "n":
                        sprint("Ok, thanks for using the program, "+username+"!")
                        sprint("See ya!")
                        end = True
                        finish = True
                    else:
                        sprint("You can only enter \'y\' or \'n\'...")
                        end = False

            #checks if the player
            else:
                sprint("You gotta enter a, b, or c")
                sprint("a: higher")
                sprint("b: lower")
                sprint("c: yes")
                finish = False
#-------------------------------------------------------------------------------------------------------------------
def MathGame():
    sprint("Hi, "+username+", let's solve some math problems!")
    sprint("You have 3 seconds to think for each question.")

    #define bunch of spaces
    def spaceBlank( str ):
        return print("\n"*100)

    #define addition problem
    def addition():
        #set two random numbers and calculate them
        number1 = random.randint(1,200)
        number2 = random.randint(1,200)
        additionanswer = number1 + number2

        #print the question and start count down
        try:
            print(str(number1)+ "+" + str(number2))
            print("1")
            count = 1
            time.sleep(1.5)
            print("2")
            count = 2
            time.sleep(1.5)
            print("3")
            count = 3
            time.sleep(1.5)
            spaceBlank( str )

            #after count 3, it prints bunch of spaces and asks for answer
            addition = input("What is your answer?: ")
            #checks if the player entered nothing
            if addition == '':
                sprint("Duh, can you not even enter anything?")
                sprint("The correct answer was, "+str(additionanswer)+"!")
            #checks if the player entered the correct answer
            elif float(addition) == additionanswer:
                sprint("Yeah~!")
            #checks if the player entered the wrong answer
            elif float(addition) != additionanswer:
                sprint("Duh~!")
                sprint("The correct answer was, "+str(additionanswer)+"!")
        #checks if the player entered in number
        except ValueError:
                sprint("You should enter in number")
        return(print("----------------------------------------------------------------------"))

    #same as addition but changed as subtraction
    def subtraction():
        number1 = random.randint(1,100)
        number2 = random.randint(1,number1)
        subtractionanswer = number1 - number2
        try:
            sprint(str(number1)+ "-" + str(number2)+": ")
            sprint("1")
            count = 1
            time.sleep(1.5)
            sprint("2")
            count = 2
            time.sleep(1.5)
            sprint("3")
            count = 3
            time.sleep(1.5)
            spaceBlank( str )

            subtraction = input("What is your answer?: ")
            if subtraction == "":
                sprint("Duh, can you not enter anything?")
                sprint("The correct answer was, "+str(subtractionanswer)+"!")
            if float(subtraction) == subtractionanswer:
                sprint("Yeah~!")
            elif float(subtraction) != subtractionanswer:
                sprint("Duh~!")
                sprint("The correct answer was, "+str(subtractionanswer)+"!")
        except ValueError:
            sprint_2("You should enter in number...")
        return(print("----------------------------------------------------------------------"))

    #same but multiplication
    def multiplication():
        number1 = random.randint(1,20)
        number2 = random.randint(1,20)
        multiplicationanswer = number1 * number2
        try:
            sprint(str(number1)+ "x" + str(number2)+": ")
            sprint("1")
            count = 1
            time.sleep(1.5)
            sprint("2")
            count = 2
            time.sleep(1.5)
            sprint("3")
            count = 3
            time.sleep(1.5)
            spaceBlank( str )

            multiplication = input("What is your answer?: ")
            if multiplication == "":
                sprint("Duh, can you not enter anything?")
                sprint("The correct answer was, "+str(multiplicationanswer)+"!")
            if float(multiplication) == multiplicationanswer:
                sprint("Yeah~!")
            elif float(multiplication) != multiplicationanswer:
                sprint("Duh~!")
                sprint("The correct answer was, "+str(multiplicationanswer)+"!")
        except ValueError:
            sprint("you better enter in number")
        return(print("----------------------------------------------------------------------"))

    #almost same #get two random numbers and multiply them #Then divide the muliplied value by the one of two random numbers
    def division():
        number1 = random.randint(1,20)
        number2 = random.randint(1,20)
        number3 = (number1*number2)
        try:
            sprint(str(number3)+ "/" + str(number1)+": ")
            sprint("1")
            count = 1
            time.sleep(1)
            sprint("2")
            count = 2
            time.sleep(1)
            sprint("3")
            count = 3
            time.sleep(1)
            spaceBlank( str )

            division = input("What is your answer?: ")
            if division == "":
                sprint("Duh, can you not enter anything?")
                sprint("The correct answer was,"+str(number2)+"!")
            if float(division) == number2:
                sprint("Yeah~!")
            elif float(division) != number2:
                sprint("Duh~!")
                sprint("The correct answer was, "+str(number2)+"!")
        except ValueError:
            sprint("You better enter in number")
        return(print("----------------------------------------------------------------------"))

    #redo
    start = True
    while start == True:
        list = input("Choose either \'addition\', \'subtraction\', \'multiplication\', \'division\', or \'exit\':")
        if list == "addition":
            addition()
        elif list == "subtraction":
            subtraction()
        elif list == "multiplication":
            multiplication()
        elif list == "division":
            division()
        elif list == "exit":
            sprint("I hope you had some fun with math! See you later!")
            start = False
        else:
            sprint("Duh, there is no option for "+list+".\nYou can only enter \'addition\', \'subtraction\', \'multiplication\', \'division\', or \'exit\'")

#-------------------------------------------------------------------------------------------------------------------
#provide bunch of spaces to hide the previous texts
def space():
    return print("\n"*50)

#-------------------------------------------------------------------------------------------------------------------
#define redo for GAMES
def redo():
    start = True
    while start == True:
        final = False
        while final == False:
            print("Do you want to play another games?(y/n):")
            #checks if input starts with y or not
            return input().startswith('y')

#-------------------------------------------------------------------------------------------------------------------

#lists
alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
gamelist=["Hangman", "Guess the Number", "Guess the Number-Reversed", "Math Game"]


sprint("You can choose either \'Hangman\', \'Guess the Number\', \'Guess the Number-Reversed\', or \'Math Game\'.")
start=False
while start == False:
    game=input("What game would you like to play?:")
    #if input is hangman, run the defined hangman game
    if game == "Hangman":
        start = True
        space()
        print(hangman( str ))
        space()
        #redo
        if redo():
            final = True
            start = False
        else:
            sprint("Alright then! Thank you for using my GAMES!")
            final = True
            break

    #if input is guess the number, run the defined guess the number game
    elif game == "Guess the Number":
        start = True
        space()
        print(GuessTheNumber( str ))
        space()
        #redo
        if redo():
            final = True
            start = False
        else:
            sprint("Alright then! Thank you for using my GAMES!")
            final = True
            break
    #if input is guess the number reversed, run the defined guess the number game

    elif game == "Guess the Number-Reversed":
        start = True
        space()
        print(GuessTheNumber_Reversed( str ))
        space()
        #redo
        if redo():
            final = True
            start = False
        else:
            sprint("Alright then! Thank you for using my GAMES!")
            final = True
            break

    #if input is math game, run the defined guess the math game
    elif game == "Math Game":
        start = True
        space()
        print(MathGame())
        space()
        #redo
        if redo():
            final = True
            start = False
        else:
            sprint("Alright, "+username+"! Thank you for using my GAMES!")
            final = True
            break

    #checks if input is in the lists(if words and in gamelist)
    elif game not in alphabets or gamelist:
        sprint("You can only enter either \'"+gamelist[0]+"\', \'"+gamelist[1]+"\', \'"+gamelist[2]+"\' or \'"+gamelist[3]+"\'")
        start = False