#!/usr/bin/env Python
import sqlite3
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')
print(f'First rows: {df.head()}')
print(f'Shape: {df.shape}')
print(f'Missing values: \n {df.isnull().sum()}')
print(f'df.describe: \n {df.describe()}')

#Open a connection to a new (blank) database file buddymove_holidayiq.sqlite3
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

#Use df.to_sql (documentation) to insert the data into a new table review in the SQLite3 database
conn.execute("DROP TABLE IF EXISTS review")
df.to_sql('review', con=conn)
conn.execute("SELECT * FROM review").fetchall()

#Then write the following queries (also with sqlite3) to test:

#Count how many rows you have - it should be 249!
cursor = conn.cursor()
how_many_rows = "SELECT COUNT('User Id') FROM review"
print(f'How many rows: {str(cursor.execute(how_many_rows).fetchall()[0][0])}')

# How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?
superuser_count = "SELECT count('User Id') \
   FROM review \
   WHERE Shopping > 100 \
   AND Nature > 100"

print(f'Superusers: {str(cursor.execute(superuser_count).fetchall()[0][0])}')

#(Stretch) What are the average number of reviews for each category?
averages = "SELECT AVG(Shopping) AS 'Shopping', \
    AVG(Picnic) AS 'Picnic', \
    AVG(Sports) AS 'Sports', \
    AVG(Religious) AS 'Religious', \
    AVG(Nature) AS 'Nature', \
    AVG(Theatre) AS 'Theatre' \
    FROM review" 
print(str(cursor.execute(averages).fetchall()))

print(df.Shopping.mean())