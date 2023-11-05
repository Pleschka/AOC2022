import numpy as np



text_file = open("input_3.txt", "r")
lines = text_file.read().split('\n')

data = np.array(lines)

Values = {}
alphabet = ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
for i in range(len(alphabet[0])):
    Values[alphabet[0][i]] = (i+1)

Score = np.array([0])
for i in range(len(data)):

    List_of_numbers = []
    for j in range(len(data[i])):
        List_of_numbers.append(Values[data[i][j]])

    for k in range(int(len(data[i])/2)):
        if List_of_numbers[k] in List_of_numbers[int(len(data[i])/2):]:
            Score += (List_of_numbers[k])
            break

print('Final sum of priority scores is', Score)

#########################
####### PART TWO ########
#########################

testarray = np.array([])
Score = np.array([0])
for i in range(0,len(data),3):

    LOS1 = []
    LOS2 = []
    LOS3 = []
    for j in range(len(data[i])):
        LOS1.append(Values[data[i][j]])
    for j in range(len(data[i+1])):  
        LOS2.append(Values[data[i+1][j]])
    for j in range(len(data[i+2])):       
        LOS3.append(Values[data[i+2][j]])

    for k in range(int(len(data[i]))):
        if LOS1[k] in LOS2 and LOS1[k] in LOS3:
            Score += (LOS1[k])
            print(i,'          ', LOS1[k],'          ',Score)
            break
        
print('Final sum of badge prioritys is', Score)