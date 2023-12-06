import pandas as pd

# Step 1: Read the sp500.csv file
df = pd.read_csv('sp500.csv')

# Step 2: Calculate the maximum value of the second column
max_value = df.iloc[:, 1].max()

print("The maximum value in the second column is:", max_value)

# Step 3: Caclute the minimum value of the second column

