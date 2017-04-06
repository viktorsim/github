# 0405 Make a number baseball game

import random

def getCipher() :
    print 'input the number of cipher.',
    cipher = raw_input()
    cipher = int(cipher)
    return cipher

def getSecretNumber() :
    i = 0
    secretNumber = []
    while i != cipher :
        n = str(random.randint(0,9))
        secretNumber.append(n)
        while secretNumber[0] == '0' :
            secretNumber[0] = str(random.randint(1,9))
        while secretNumber[i] in secretNumber[:i] :
            secretNumber[i] = str(random.randint(0,9))
        i = i + 1
    return secretNumber

def getGuessedNumber() :
    guess = []
    while True :
        print 'Guess numbers : ',
        
        userNum = raw_input()
        while len(userNum) != cipher :
            print 'Please enter a ' + str(cipher) + '-cipher number.'
            print 'Guess numbers : ',
            userNum = raw_input()
            
        guess = userNum
        if guess in guessedNumbers :
            print 'You have already guessed that number. Choose another number.'
            print 'Guess numbers : '
            
        n = 1
        while n != len(str(userNum)) :
            if guess[n] in guess [:n]:
                print 'There are repeated numbers. Choose another number.'
                print 'Guess numbers : ',
            elif guess[n] in guess [n+1:] :
                print 'There are repeated numbers. Choose another number.'
                print 'Guess numbers : ',
            n = n + 1
            
        if guess[0] == '0' :
            print 'Please enter a ' + str(cipher) + '-cipher number.'
            print 'Guess numbers : ',

        return guess
        
def checkStrike() :
    n = 0
    strike = 0
    while n != cipher :
        if guess[n] == secretNumber[n] :
            strike = strike + 1
        n = n + 1
        
    if strike == cipher :
        print 'You win. Secret number is ',
        
        print secretNumber[:n+1]
        gameIsDone = True
        
    return strike

def checkBall() :
    n = 0
    ball = 0
    while n != cipher :
        if guess[n] in secretNumber[:n] :
            ball = ball + 1
        elif guess[n] in secretNumber[n+1:] :
            ball = ball + 1
        n = n + 1
    return ball

def displayBoard(strike, ball) :
    print 'strike : ' + str(strike) + '\nball : ' + str(ball)

def playAgain() :
    print 'Do you want to play again? (yes or no)'
    return raw_input().lower().startswith('y')

        

#total code
guessedNumbers = []

print 'S  T  A  R  T'
gameIsDone = False

cipher = getCipher()
secretNumber = getSecretNumber()
print secretNumber

while True :
    guess = getGuessedNumber()
    guessedNumbers.append(guess)
    ball = checkBall()
    strike = checkStrike()
    if strike == cipher :
        gameIsDone = True
    else :
        displayBoard(strike, ball)

    if gameIsDone == True :
        if playAgain() :
            guessedNumbers = []
            strike = 0
            ball = 0
            gameIsDone = False
            cipher = getCipher()
            secretNumber = getSecretNumber()
            print secretNumber
        else :
            break
        

    
