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

'''
2. Insert values into table from these lists:
----Names: "COPD", "Bronchitis", "Diabetes", "Alzheimer's", "Tuberculosis"
----Cases: 251, 9, 425, 44, 10
----Deaths: 3000000, 20000, 1600000, 100000, 1500000
----Mortality: 0.7, 0.5, 0.15, 0.37, 0.24
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
    ("Bronchitis", 9, 20000, 0.5),
    ("Diabetes", 425, 1600000, 0.15),
    ("Alzheimer's", 44, 100000, 0.37),
    ("Tuberculosis", 10, 1500000, 0.24);
'''

curs.execute(drop_table)

curs.execute(create_table)

curs.execute(insert_values)
conn.commit()
