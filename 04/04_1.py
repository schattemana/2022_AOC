import pandas as pd


data = pd.read_csv('04\input.txt',
                   sep="-|;|:|,",
                   header=None,
                   engine='python')

data['diff_one'] = data[0] - data[2] 
data['diff_two'] = data[1] - data[3]
data['inside'] = (data['diff_one'] <= 0) & (data['diff_two'] >= 0) | (data['diff_one'] >=0) & (data['diff_two'] <= 0)

total = sum(data['inside'])





#2
data['overlap'] = (data[1] >= data[2]) & (data[0] <= data[2]) | (data[3] >= data[0]) & (data[2] <= data[1])
total_overlap = sum(data['overlap'])

print(data, total, total_overlap)
