#!/opt/anaconda3/bin Python

from functools import reduce
import sqlite3

my_list = [1, 2, 3, 4]

# Approach without mapreduce - loop over it
ssv_trad = sum([i ** 2 for i in my_list])

squared_values = map(lambda i: i ** 2, my_list)


def add_numbers(x1, x2):
    return x1 + x2


ssv_mapreduce = reduce(add_numbers, squared_values)

print('trad ' + str(ssv_trad))
print('map-reduce ' + str(ssv_mapreduce))

# Other thing, creating and inserting data

conn = sqlite3.connect('playground.sqlite3')


def insert_data(conn):
    my_data = [
        ('Thorbaald', 7, 10),
        ('Svengren', -3, 12),
        ('Grenalffssen', 80, -1)
    ]
    curs = conn.cursor().insert_many(
        [{k: v for k, v in zip(my_data)}]
    )


def create_table(conn):
    curs = conn.cursor()
    create_statement = """
    CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name CHAR(20),
    favorite_number INTEGER
    least_favorite_number INTEGER
    );
    """
    curs.execute(create_statement)
    curs.close()
    curs.commit()


if __name__ == '__main__':
    conn = sqlite3.connect('playground.sqlite3')
