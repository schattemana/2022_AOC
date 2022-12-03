import string

with open('03\input.txt') as f:
    lines = f.read().splitlines() 

def find_priority(letter):
    if letter in string.ascii_lowercase:
        return ord(letter) - 96
    else:
        return ord(letter) - 38



itemstring = ''

for line in lines:
    first_half  = line[:len(line)//2]
    second_half = line[len(line)//2:]
    for character in first_half:
        if character in second_half:
            itemstring += character
            break
        


total_priority = 0
for item in itemstring:
    total_priority += find_priority(item)


print(total_priority)

