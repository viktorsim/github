#dotdotdotdotdot 15 March 2017

#    blank 4 + star 1
#    blank 3 + star 1 + blank 1 + star 1
#    blank 2 + star 1 + blank 3 + star 1
#    blank 1 + star 1 + blank 5 + star 1
#    blank 0 + star 9

firstBlank = 4
secondBlank = -1
lines = 0

while lines < 4 :
    print ' '*firstBlank,
    print '*',
    if secondBlank >= 0 :
        print ' '*secondBlank,
        print '*',
    print ''
    firstBlank = firstBlank -1
    secondBlank = secondBlank +2
    lines = lines + 1

print '*'*9
