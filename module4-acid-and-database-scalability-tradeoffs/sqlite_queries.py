#!/usr/bin/env Python
import sqlite3

# Connection will make a new database called 'review.sqlite3'.
# You should delete this file before you run the script again.
conn = sqlite3.connect('review.sqlite3')
curs = conn.cursor()

'''
1. Create a table called "disease"
----Columns:
    - name (a string - 20 characters max)
    - cases_in_millions (an integer)
    - deaths (an integer)
    - mortality_rate (a float)

***Make sure to add a condition to the statement
***for reproducibility (running multiple times)
'''
drop_table = '''
DROP TABLE IF EXISTS disease;
'''

create_table = '''
CREATE TABLE disease (
    name VARCHAR(20),
    cases_in_millions INT,
    deaths INT,
    mortality_rate FLOAT
);
'''

insert_values = '''
INSERT INTO disease (
    name,
    cases_in_millions,
    deaths,
    mortality_rate
)
VALUES
    ("COPD", 251, 3000000, 0.7),
    ("bronchitis", 9, 2000, 0.5),
    ("Diabetes", 425, 1600000, 0.15),
    ("Alzheimer's", 44, 100000, 0.37),
    ("Tuberculosis", 10, 1500000, 0.24)
'''

curs.execute(create_table)
curs.execute(insert_values)
curs.commit()