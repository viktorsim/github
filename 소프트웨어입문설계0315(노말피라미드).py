#dotdotdotdotdot 15 March 2017
#moraesigye

lines = 0
blanks = 0
stars = 9
while lines < 5 :
    lines = lines + 1
    print ' '*blanks,
    print '*'*stars
    stars = stars - 2
    blanks = blanks + 1

lines = 1
stars = 1
blanks = 4
while lines < 5 :
    lines = lines + 1
    blanks = blanks - 1
    stars = stars + 2
    print ' '*blanks,
    print '*'*stars
