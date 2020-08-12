#!/opt/anaconda3/bin Python

import sqlite3

# Open connection to new blank database file
conn = sqlite3.connect('demo_data.sqlite3')

# Make a cursor
curs = conn.cursor()

drop_table = '''
DROP TABLE IF EXISTS demo;
'''
# Write appropriate CREATE TABLE statement
create_table = '''
CREATE TABLE demo(
    s VARCHAR(10),
    x INT,
    y INT
);
'''

# Write appropriate INSERT INTO statements
insert_values = '''
INSERT INTO demo (
    s,
    x,
    y
)
VALUES
("g", 3, 9),
("v", 5, 7),
("f", 8, 7);
'''
# Execute and commit
curs.execute(drop_table)
curs.execute(create_table)
curs.execute(insert_values)
conn.commit()

# Test queries
curs.execute('SELECT COUNT (*) FROM demo;')
print(f'Rows: {curs.fetchall()[0][0]}')
'''
ANSWER how many rows: 3 rows
'''

curs.execute('SELECT COUNT(*) FROM DEMO WHERE x>=5 AND y>=5;')
print(f'Rows where x, y >= 5: {curs.fetchall()[0][0]}')
'''
ANSWER rows where x>=5 and y>=5: 2 rows
'''

curs.execute('SELECT COUNT(DISTINCT y) FROM demo')
print(f'Unique values of y: {curs.fetchall()[0][0]}')
'''
ANSWER unique values of y: 2
'''