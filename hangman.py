import random
import re

drawing = [[' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ']]

answer = ""
dash = ""
lock = False
count = 0
lstletter = []

def countingwords():
    wordcount = 0
    with open ('newwords.txt', 'r') as f:
        for line in f:
            wordcount += 1
    return wordcount #1, 2, 3 etc

def randomword(wordcount):
    global answer
    global dash
    with open ('newwords.txt', 'r') as f:
        lst = []
        num = random.randint(1, wordcount)
        for line in f:
            lst.append(line)
    answer = (lst[num]).lower()
    dash = "_ " * (len(lst[num]) - 1)
    return answer #get the word

def wordlength(word):
    print('The word has ' + str(dash.count("_ "))+ ' letters left')
    print(dash)
    print('Pick a letter')

def get_input():
    global dash
    global count
    global lstletter
    guess = str(input())
    if guess in dash and len(guess) == 1:
        print('Letter already guessed')
    elif guess in answer and len(guess) == 1:
        print('You have guessed a letter')
        lst = get_position(answer, guess)
        for i in lst:
            lstdash = list(dash.replace(' ', ''))
            lstdash[i] = guess
            dash = " ".join(lstdash)
    if len(guess) > 1:
        print('Unsupported input')
    elif guess not in answer:
        print("Wrong input, please try again")
        count += 1
        lstletter.append(guess)
        draw()
        
def draw():
    global count
    if count == 1:
        print('You have 5 lives left')
        for i in range(0, 7):
            drawing[i][0] = "N"
    if count == 2:
        print('You have 4 lives left')
        for i in range(2, 5):
            drawing[i][1] = "N"
    if count == 3:
        print('You have 3 lives left')
        for i in range(0, 7):
            drawing[i][2] = "N"
    if count == 4:
        print('You have 2 lives left')
        for i in range(1, 6):
            drawing[i][3] = "O"
    if count == 5:
        print('You have 1 lives left')
        drawing[0][4] = "O"
        drawing[6][4] = "O"
    if count == 6:
        print('You have 0 lives left')
        for i in range(1, 6):
            drawing[i][5] = "O"
        youdied()

def youdied():
    print('You lost')
    print('Play another? Enter Y or N')
    uinput = input()
    if uinput == 'Y' or uinput == 'y':
        game_logic()
    else: 
        quit()
  
def get_position(word, letter):
    lst = []
    for i in range(len(word)):
        if word[i] == letter:
            lst.append(i)
    return lst
                   
def check_state():
    global lock
    global dash
    if "_" not in dash:
        print(dash)
        lock = True
        

def game_logic():
    global lock
    global answer
    global lstletter
    reset()
    wordcount = countingwords()
    word = randomword(wordcount)
    while lock == False:
        for row in drawing:
            print(row)
        print('Here are a list of guessed letters')
        print(lstletter)
        wordlength(word)
        get_input()
        check_state()
        print('\n')
    print('You Won')
    print('Play another? Enter Y or N')
    uinput = input()
    if uinput == 'Y' or uinput == 'y':
        game_logic()
    else: 
        quit()

def reset():
    global dash
    global lock
    global count
    global drawing
    global lstletter
    dash = ""
    lock = False
    count = 0
    lstletter = []
    drawing = [[' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' '],
               [' ', ' ', ' ', ' ', ' ', ' ']]
    print('\n')
    
game_logic()
