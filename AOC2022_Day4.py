import numpy as np



text_file = open("input_4.txt", "r")
lines = text_file.read().split('\n')

data = np.array(lines)

Total = np.array([0])
Total = 0

for i in range(len(data)):
    counter = 0
    Numbers = [[],[],[],[]]
    for j in range(len(data[i])):
        Placeholder = ''
        if data[i][j] == '-' or data[i][j] == ',':
            for k in range(len(Numbers[counter])):
                Placeholder = Placeholder + Numbers[counter][k]
            Numbers[counter] = float(Placeholder)
            counter += 1
        else:  
            Numbers[counter].append(data[i][j])
            
    Placeholder = ''        
    for n in range(len(Numbers[counter])):
        Placeholder = Placeholder + Numbers[counter][n]
    Numbers[counter] = float(Placeholder)
    A = range(Numbers[0],Numbers[1])
    B = range(Numbers[1],Numbers[2])
    if A        
   

