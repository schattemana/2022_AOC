import string


def find_priority(letter):
    if letter in string.ascii_lowercase:
        return ord(letter) - 96
    else:
        return ord(letter) - 38


with open('03\input.txt') as f:
    lines = f.read().splitlines() 

line_sets = []
for line in lines:
    line = set(line)
    line_sets.append(line)

groups = [line_sets[i:i + 3] for i in range(0, len(line_sets), 3)]

common_items = []
for group in groups:
    item = list(group[0].intersection(group[1], group[2]))
    common_items.append(item[0])

total_priority = 0
for item in common_items:
    total_priority += find_priority(item)


print(total_priority)


