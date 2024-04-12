# Concatenate strings from multiple rows with Pandas GroupBy

import pandas as pd

df = pd.DataFrame({
    'Name': [
        'Alice',
        'Bobby',
        'Carl',
        'Dan',
        'Ethan'
    ],
    'Date': [
        '2023-07-12',
        '2023-07-12',
        '2023-08-23',
        '2023-08-21',
        '2023-08-23'
    ]
})


#     Name        Date
# 0  Alice  2023-07-12
# 1  Bobby  2023-07-12
# 2   Carl  2023-08-23
# 3    Dan  2023-08-21
# 4  Ethan  2023-08-23
print(df)

print('-' * 50)


df['Name'] = df.groupby(['Date'])['Name'].transform(','.join)

df = df[['Name', 'Date']].drop_duplicates()

#           Name        Date
# 0  Alice,Bobby  2023-07-12
# 2   Carl,Ethan  2023-08-23
# 3          Dan  2023-08-21
print(df)