# 0405 Number Baseball Game(3-digit number)
import random

def getSecretNumber() : # to make a 3-digit secret number
    digit1 = random.randint(1, 9)
    digit2 = random.randint(0, 9)
    while digit1 == digit2 :
        digit2 = random.randint(0, 9)
    digit3 = random.randint(0, 9)
    while digit3 == digit1 or digit3 == digit2 :
        digit3 = random.randint(0, 9)
    
    secretNumber = [digit1, digit2, digit3]
    return secretNumber

def getNumber() : # to input user's number
    while True :
        print 'Guess numbers(000~999) :'
        userNum = raw_input()
        userNum = int(userNum)

        guessedDigit1 = userNum / 100
        guessedDigit2 = (userNum / 10) % 10
        guessedDigit3 = userNum % 10
        guess = [guessedDigit1, guessedDigit2, guessedDigit3] # list to divide userNum by digit.

        if len(str(userNum)) != 3 :
            print 'Please enter a 3-digit number.'
        elif guess in guessedNumbers :
            print 'You have already guessed that number. Choose another number.'
        elif guess[0] == guess[1] or guess[0] == guess[2] or guess[1] == guess[2] :
            print 'There are repeated number. Choose another number.'
        elif guess[0] == 0 :
            print 'Please enter a 3-digit number which is more than 100'
        else :
            return guess

def checkStrike():
    strike = 0
    if guess[0] == secretNum[0] :
        strike = strike + 1
    if guess[1] == secretNum[1] :
        strike = strike + 1
    if guess[2] == secretNum[2] :
        strike = strike + 1
        if strike == 3 :
            print 'You win. Secret number is ' + str(secretNum)
    return strike

def checkBall() :
    ball = 0
    if guess[0] == secretNum[1] or guess[0] == secretNum[2] :
        ball = ball + 1
    if guess[1] == secretNum[0] or guess[1] == secretNum[2] :
        ball = ball + 1
    if guess[2] == secretNum[0] or guess[2] == secretNum[1] :
        ball = ball + 1
    return ball


def displayBoard(strike, ball) :
    print 'strike : ' + str(strike) + '  ball : ' + str(ball)

def playAgain() :
    print 'Do you want to play again? (yes or no)'
    return raw_input().lower().startswith('y')








# totally
guessedNumbers = []

print 'S T A R T'
secretNum = getSecretNumber()
print secretNum
gameIsDone = False

while True :
    guess = getNumber()
    guessedNumbers.append(guess)
    strike = checkStrike()
    if strike == 3 :
        gameIsDone = True
    ball = checkBall()

    if gameIsDone == True :
        if playAgain() :
            guessedNumbers = []
            strike = 0
            ball = 0
            gameIsDone = False
            secretNum = getSecretNumber()
        else :
            break
    
    displayBoard(strike, ball)
