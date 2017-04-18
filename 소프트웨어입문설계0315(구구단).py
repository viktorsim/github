#99dan game. 15 March 2017
import random
import time

print '********** Start ***********'
repeat = 0

while repeat < 5 :
    repeat = repeat + 1
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    num3 = random.randint(1, 9)
    num4 = random.randint(1, 9)
    num1 = str(num1)
    num2 = str(num2)
    num3 = str(num3)
    num4 = str(num4)

    print(num1 + ' * ' + num2 + ' + ' + num3 + ' - ' + num4 + ' = ?')
    time.sleep(1)
    print '1, ',
    time.sleep(1)
    print '2, ',
    time.sleep(1)
    print '3. ',
    
    answer = raw_input()
    answer = int(answer)
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    num4 = int(num4)
    correct = num1*num2+num3-num4

    if answer == correct :
        print 'Correct Answer'
    if answer != correct :
        num1 = str(num1)
        num2 = str(num2)
        num3 = str(num3)
        num4 = str(num4)
        correct = str(correct)
        print 'Wrong Answer, ' + num1 + ' * ' + num2 + ' + ' + num3 + ' - ' + num4 + ' = ' + correct
