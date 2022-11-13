import pandas as pd


# df = pd.read_excel('users.xlsx')
df = pd.read_excel('users.xlsx', sheet_name='purchase', index_col=0, header=3)
# df = pd.read_excel('users.xlsx', sheet_name=[0, 2])

print(df)