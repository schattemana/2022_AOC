import pandas as pd

# Task 1
df = pd.read_csv("08\input.txt", header=None)

# Get the first column of the DataFrame
column = df.iloc[:, 0]

# Define a function that takes in a string and returns a Series of characters
def split_string(string):
    return pd.Series(list(string))

# Apply the function to each element of the column
df = column.apply(split_string)



rows = len(df)
cols = len(df.columns)
visible = 0
for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        size = df.iloc[row, col]

        up = df.iloc[:row, col]
        down = df.iloc[row + 1 :, col]
        left = df.iloc[row, :col]
        right = df.iloc[row, col + 1 :]

        

        if size > max(up) or size > max(down) or size > max(left) or size > max(right):
            visible += 1

total_visible = rows * 4 - 4 + visible
print("Visible: ", total_visible)

