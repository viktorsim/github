# 0405 Make a number baseball game

import random
import time

def openingDisplay() :
    print "In an eodup and eumchim night..."
    time.sleep(1)
    print "Walking around College of Humanity, you meet a big bear!"
    time.sleep(1)
    print 'Run?(1) or Fight?(2)'
    chooseFirst = raw_input()
    return chooseFirst

def run() :
    chooseRun = random.randint(1,2)
    return chooseRun

def runSuccess() :
    print "You've run from the bear successfully!"


def fight() :
    print 'You and your friend must kill the bear within 7 attacks.'
    print "If you and your friend's are equal, it will be three-times damage."
    print "Let's fight!"

    i = 0
    bear = 100
    while i != 7 and bear > 0 :
        you = random.randint(0, 9)
        friend = random.randint(0, 9)
        if you == friend :
            you = you * 3
            friend = friend * 3
        bear = bear - you - friend
        print 'you attacked ' + str(you) + ' damages.'
        print 'your friend attacked ' + str(friend) + 'damages.'
        if bear <= 0 :
            print 'You and your friend killed the bear.'
        else :
            i = i + 1
    



def playAgain() :
    print 'Play Again? ',
    raw_input.lower.startswith('y')



#totally
gameIsDone = False
while True :
    choose = openingDisplay()
    if choose == 1 :
        chooseRun = run()
        if chooseRun == 1 :
            runSuccess()
            gameIsDone = True
        elif chooseRun == 2 :
            fight()

    if gameIsDone == True:
        playAgain()
        gameIsDone = False
