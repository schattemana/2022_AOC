#part one
with open('02\input.txt') as f:
    lines = f.readlines()

WLD_dict = {6: ['A Y', 'B Z', 'C X'], 0: ['A Z', 'B X', 'C Y'], 3: ['A X', 'B Y', 'C Z']}
value_dict = {1: 'X',2: 'Y', 3:'Z'}


total_WLD = 0
total_value = 0
for line in lines:
    line = line.rstrip()
    for key in value_dict:
        if line[-1] in value_dict[key]:
            total_value += key


    for key in WLD_dict:
        if line in WLD_dict[key]:
            total_WLD += key
print(total_WLD, total_value, total_WLD+total_value)



    
