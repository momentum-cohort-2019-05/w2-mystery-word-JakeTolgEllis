

import random


def split(word):
    '''
    input: word that you want to be split into list
    output: said list
    '''
    lis = []
    for i in range(len(word)):
        lis.append(word[i])
    return(lis)

def init(mysterySplit):
    '''
    initializes the progress line 
    '''
    state = []
    for i in range(len(mysterySplit)):
        state.append("_ ")
    
    return(state)
    
#def checkIf(guess, mysterySplit):
#    for idx in range(len(mysterySplit)):
#            if guess == mysteryWord:
#                digit = idx
 #               return(int(digit))
    
#def function(init, mysterySplit, correctIndex):
    '''
    input: List of each character of the guess input string
    output: Current state of mystery Word
    '''
    
    #for i in range(len(mysterySplit)):
        
    

#initalizes the file, and loads all the words into words list as strings
file = open('words.txt','r')
words = file.read()
words = words.split()

#Gamemode
mode = str(input("How hard do you want this thing to be? (e)asy, (m)edium, or, (i)mpossible? "))

if mode == "e":
    flag = True
    while flag == True:
        randomNumber = random.randint(0,len(words) - 1)
        if len(words[randomNumber]) >= 4 and len(words[randomNumber]) <= 6:
            break
                
if mode == "m":
    flag = True
    while flag == True:
        randomNumber = random.randint(0,len(words))
        if len(words[randomNumber]) >= 6 and len(words[randomNumber]) <= 8:
            break
                
if mode == "i":
    flag = True
    while flag == True:
        randomNumber = random.randint(0,len(words))
        if len(words[randomNumber]) >= 8:
            break
                
worldLength = str(len(words[randomNumber]))
mysteryWord = str(words[randomNumber])
mysterySplit = split(mysteryWord)

#initializes guess listi and main to be used in the while loop
guessList = []
main = init(mysterySplit)
mainString = ''.join(main)
counter = 0
#main loop of game. Runs so long as flag is false. initializes 
flag = True
while flag == True:
    #have user take a guess
    guess = str(input("Take a guess, the mystery word is " + worldLength + " letters long. \nGuess:"))
        
    if len(guess) > 1:
        print("Invalid input. You can only guess single letters. Try again.")
        continue
    
    for idx in range(len(mysterySplit)):
        if mysterySplit[idx] == guess:
            main[idx] = guess

   # digit = int(checkIf(guess, mysterySplit))
        
    
    if guess in guessList:
        print("\nYou have already guessed this, dingus.")
        continue
    
    guessList.append(guess)
    
    
    
    #progress = function(main, digit)
    
    if guess in mysterySplit:
        print("\nCorrect! \n")
        print("Your guesses:\n")
        print(guessList)
        print("Mystery Word!: " + str("".join(main)))
        
    if guess not in mysterySplit:
        print("\nIncorrect! \n")
        print("Your guesses:\n")
        print(guessList)
        print("\nMystery Word!: " + str("".join(main)))
        
    if str("".join(main)) == mysteryWord:
        print("Congratulations, friend, you've won.")
        break

    counter += 1
    if counter > 8:
        print("You've lust, dummmmmyyyy boooooiiiiiiii")
        break
    


    