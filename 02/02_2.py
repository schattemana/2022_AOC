with open('02\input.txt') as f:
    lines = f.readlines()

WLD_dict = {6: 'Z', 0: 'X', 3: 'Y'}

def pick_element(line):

    value_dict = {1: 'A',2: 'B', 3:'C'}

    if line[-1] == 'Y':
            element = line[0]
    elif line[-1] == 'X':
        if line[0] == 'A':
            element = 'C'
        if line[0] == 'B':
            element = 'A'
        if line[0] == 'C':
            element = 'B'
    elif line[-1] == 'Z':
        if line[0] == 'A':
            element = 'B'
        if line[0] == 'B':
            element = 'C'
        if line[0] == 'C':
            element = 'A'
    
    for key in value_dict:
        if element in value_dict[key]:
            return key

        



total_WLD = 0
total_value = 0
for line in lines:
    line = line.rstrip()
    total_value += (pick_element(line))
#get scores for winning or losing
    for key in WLD_dict:
        if line[-1] in WLD_dict[key]:
            total_WLD += key

print(total_WLD, total_value, total_WLD + total_value)