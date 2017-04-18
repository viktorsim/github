# 0405 Make a number baseball game

import random
import time

def getCipher() :
    print 'The number of cipher : ',
    time. sleep(1)
    cipher = random.randint(1, 9)
    print str(cipher)
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
        print 'Guessed number is ',
        
        comNum = random.randint(10**(cipher-1), 10**cipher-1)
        print  str(comNum)
            
        guess = str(comNum)
        if guess in guessedNumbers :
            print 'It is already guessed that number. I will try again...'
            
        n = 1
        while n != len(str(comNum)) :
            if guess[n] in guess [:n]:
                print 'There are repeated numbers. Choose another number.1'
            elif guess[n] in guess [n+1:] :
                print 'There are repeated numbers. Choose another number.2'
            n = n + 1

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
        for i in secretNumber :
            print i,
        print
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
time.sleep(2)
print 'cipher : ' + str(cipher)
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
        

    
