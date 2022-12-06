text_file = open("06\input.txt", "r")

#read whole file to a string
data = text_file.read()
llist = []
count = 0
for i in range(len(data)):
    count = 0

    for letter in data[i:i+14]:
        if data[i:i+14].count(letter) == 1:
            count += 1
            if count == 14:
                llist.append(data[i:i+14])
            
        else:
            count =0
print(llist)    
print(data.find(llist[0]) +14 )  