#!/usr/bin/env Python
import sqlite3
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')
print(f'First rows: {df.head()}')
print(f'Shape: {df.shape}')
print(f'Missing values: \n {df.isnull().sum()}')
print(f'df.describe: \n {df.describe()}')

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

conn.execute("DROP TABLE IF EXISTS review")
df.to_sql('review', con=conn)
# conn.execute("SELECT * FROM review").fetchall()
cursor = conn.cursor()
how_many_rows = "SELECT COUNT('User Id') FROM review"
print(f'How many rows: '
      f'{str(cursor.execute(how_many_rows).fetchall()[0][0])}')

superuser_count = "SELECT count('User Id') \
    FROM review \
    WHERE Shopping > 100 \
    AND Nature > 100"

print(f'Superusers: '
      f'{str(cursor.execute(superuser_count).fetchall()[0][0])}')

# #(Stretch) What are the average number of reviews for each category?
# averages = "SELECT AVG(Shopping) AS 'Shopping', \
#     AVG(Picnic) AS 'Picnic', \
#     AVG(Sports) AS 'Sports', \
#     AVG(Religious) AS 'Religious', \
#     AVG(Nature) AS 'Nature', \
#     AVG(Theatre) AS 'Theatre' \
#     FROM review"
# print(str(cursor.execute(averages).fetchall()))
#
# print(df.Shopping.mean())