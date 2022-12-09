import pandas as pd


data = pd.read_csv('05\input.txt',
                   sep="[|][|][",
                   header=None,
                   engine='python')
print(data)