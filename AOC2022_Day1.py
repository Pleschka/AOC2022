import numpy as np



text_file = open("input_1.txt", "r")
lines = text_file.read().split('\n')

data = np.array(lines)

Elves = np.array([])
Sum = np.zeros(1)

for i in range(len(data)):
    if data[i] == '':
        data[i] = 0
            
data = data.astype(float)

for i in range(len(data)):
    if data[i] !=  0:
        Sum += data[i]
    else:
        Elves = np.append(Elves,Sum)
        Sum = np.zeros(1)
            
Elf_max_cal = np.max(Elves)
Elf_num = np.argmax(Elves) + 1
        
print('The elf with the most food is elf number', Elf_num)
print('The elf is carrying', Elf_max_cal,' calories')

#########################
####### PART TWO ########
#########################

Sum = np.zeros(1)

for n in range(3):
    Elf_max_cal = np.max(Elves)
    Elf_num = np.argmax(Elves)
    Sum += Elf_max_cal
    Elves[Elf_num] = 0

print('The total food carried by the top 3 elves is', Sum, 'calories')