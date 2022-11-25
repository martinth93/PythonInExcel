import pandas as pd
import numpy as np
import datetime


# def main():
#     # df = pd.read_excel('users.xlsx')
#     # df = pd.read_excel('users.xlsx', sheet_name='purchase', index_col=0, header=3)
#     # df = pd.read_excel('users.xlsx', sheet_name=[0, 2])
#-
#     print(df)
#
#     # df.to_excel('saved_file.xlsx', index=False)
#
#     # f = pd.ExcelFile('users.xlsx')
#     # print(f.sheet_names)
#     # print(f.parse(sheet_name='User_info'))


# def main():
#     df = pd.read_csv("https://raw.githubusercontent.com/pythoninoffice/"
#                      "blog_example_code/main/split_excel_file/master_file.csv")
#     df_laptop = df.loc[df['sale_product'] == 'Laptop']
#     print(df_laptop.head())
#     categories = df['sale_product'].unique()
#     print(categories)
#
#     with pd.ExcelWriter('new_file.xlsx') as new_file:
#         for category in categories:
#             df.loc[df['sale_product']==category].to_excel(new_file, sheet_name=category, index=False)
#


# def main():
#     df = pd.DataFrame(np.random.randint(100, size=(20, 5)))
#     df_1 = df.loc[0:10]
#     df_2 = df.loc[11:20]
#     df_append = pd.Series([100, 100, 100, 100, 100])
#
#     print(df_append)
#
#     df_final = pd.concat([df_1, df_append.to_frame().T], ignore_index=True)
#     df_final = pd.concat([df_final, df_2])
#
#     print(df_final)


# def main():
#     df = pd.DataFrame({'col 1':[1, 2, 3, 4, 5],
#                        'col 2':[6, 7, 8, 9, 10],
#                        'col 3':[11, 12, 13, 14, 15]
#     })
#     print(df)
#
#     df.insert(1, 'new col', [100]*5)
#
#     print(df)
#
#     df['square-bracket method'] = df['new col'] * 2
#
#     print(df)
#
#     df = df.assign(col_1_x_2=df['col 1']*2)
#
#     print(df)
#
#     num_to_letter = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}
#     df['letter'] = df['col 1'].map(num_to_letter)
#
#     print(df)


# def main():
#     df = pd.read_excel('users.xlsx', index_col=0)
#     print(df)
#     print(df.drop('Harry Porter'))
#     print(df.drop(df.index[[0, 2]]))
#     print(df.index != 'Jean Gray')
#     print(df[[True, True, True, False]])
#
# def main():
#     df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
#     print(df.loc[df['GICS Sector'] == 'Information Technology'])
#     print(df.head())


# def main():
#     df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
#     df['City'] = df['Headquarters Location'].str.split(',', expand=True)[0]
#     df['State'] = df['Headquarters Location'].str.split(',', expand=True)[1]
#     df['Date first added'] = df['Date first added'].str.split('(', expand=True)[0]
#     df['Date first added'] = pd.to_datetime(df['Date first added'])
#
#     today = datetime.datetime.today()
#     days = today - df['Date first added']
#     df['Yrs on SP500'] = days.dt.days / 365
#
#     print(df.head())

# def main():
#     df = pd.read_excel('split_text.xlsx', dtype={'Name': str, 'Date of Birth': str})
#     df['First Name'] = df['Name'].str.split(',', expand=True)[1]
#     df['Last Name'] = df['Name'].str.split(',', expand=True)[0]
#     print(df)


if __name__ == "__main__":
    main()

