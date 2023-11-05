import numpy as np



text_file = open("input_2.txt", "r")
lines = text_file.read().split('\n')

data = np.array(lines)

#A,X = rock, B,Y = paper, C,Z = scissors, 
#Scores part 1: 1 for rock, 2 for paper, 3 for scisors
#Scores part 2: 0 for loss, 3 for draw, 6 for win

Scores = {'A X':4,'A Y':8,'A Z':3,'B X':1,'B Y':5,'B Z':9,'C X':7,'C Y':2,'C Z':6}

Sum = np.array([0])

for i in range(len(data)):
    Sum = Sum + Scores[data[i]]
    
print ('total score is', Sum, 'points')

#########################
####### PART TWO ########
#########################

#A = rock, B = paper, C = scissors, 
#X = loose, Y = Draw , Z = Win
#Scores part 1: 1 for rock, 2 for paper, 3 for scisors
#Scores part 2: 0 for loss, 3 for draw, 6 for win

Scores2 = {'A X':3,'A Y':4,'A Z':8,'B X':1,'B Y':5,'B Z':9,'C X':2,'C Y':6,'C Z':7}

Sum2 = np.array([0])

for i in range(len(data)):
    Sum2 = Sum2 + Scores2[data[i]]
    
print ('total adjusted score is', Sum2, 'points')