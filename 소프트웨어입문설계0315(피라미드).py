#dotdotdotdotdot 15 March 2017
#normal

line_number = 0
blank = 4
dotting = 1
while line_number < 5 :
    print (blank-line_number)*' ',
    print '*'*dotting
    line_number = line_number + 1
    dotting = dotting + 2

