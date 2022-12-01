#part one
with open('input') as f:
    lines = f.readlines()


def max_finder(lines):
    arraylist = []
    group_list = []
    sumlist = []
    for line in lines:
        line = line.rstrip()
        
        if not line == '':
            group_list.append(int(line))
        else:
            arraylist.append(group_list)
            group_list = []
    
    for item in arraylist:
        sumlist.append(sum(item))
        
    return str(max(sumlist))

print('The elf with the most calories has: ' + max_finder(lines) + ' calories')



#part two


def three_max_finder(lines):
    arraylist = []
    group_list = []
    sumlist = []
    for line in lines:
        line = line.rstrip()
        
        if not line == '':
            group_list.append(int(line))
        else:
            arraylist.append(group_list)
            group_list = []
    
    for item in arraylist:
        sumlist.append(sum(item))

    maxlist = []
    for i in range(3):
        maxlist.append(max(sumlist))
        sumlist.remove(max(sumlist))

    return str(sum(maxlist))

print('The three elfs with the most calories have: ' + three_max_finder(lines) + ' calories combined')

