import pandas as pd

# Load CSVs
df1 = pd.read_csv('followers.csv')
df2 = pd.read_csv('followers_new.csv')
# df1 = pd.read_csv('following.csv')
# df2 = pd.read_csv('following_new.csv')

# Select the column to compare
col = 'username'

# Convert to sets
set1 = set(df1[col])
set2 = set(df2[col])

# Find differences
missing_in_file2 = set1 - set2
extra_in_file2 = set2 - set1

print("Missing in file2:", missing_in_file2)
print("Extra in file2:", extra_in_file2)
