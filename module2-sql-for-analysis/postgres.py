#!/opt/anaconda3/bin Python

import os
import psycopg2
import sqlite3
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("EL_DB_NAME")
DB_HOST = os.getenv("EL_DB_HOST")
DB_PASS = os.getenv("EL_DB_PASS")
DB_USER = os.getenv("EL_DB_USER")

pg_conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
pg_curs = pg_conn.cursor()

create_statement = """
"""

insert_statement = """
INSERT INTO test_table (name, data)
VALUES (
'Zaphod Beeblebrox',
'{"key": "value", "key2": "value=2"}');
"""

selectall_statement = """
SELECT *
FROM test_table;
"""


def sqlite3_sql(dbname, statement):
    # Function to run any SQL statement
    sl_conn = sqlite3.connect(dbname)
    sl_curs = sl_conn.cursor()
    sl_curs.execute(statement)
    return sl_curs.fetchall()


database = 'rpg_db.sqlite3'
get_characters = "SELECT * FROM charactercreator_character"
sqlite3_sql(database, get_characters)
# print(len(characters))
# print(characters[:5])

# Transform
pragma_statement = """
PRAGMA table_info(charactercreator_creator);
"""
sqlite3_sql(database, pragma_statement)

create_character_table = """
CREATE TABLE charactercreator_character (
character_id SERIAL PRIMARY KEY,
name VARCHAR(30),
level INT,
exp INT,
hp INT,
strength INT,
intelligence INT,
dexterity INT,
wisdom INT
);
"""

show_tables = """
SELECT
*
FROM
pg_catalog.pg_tables
WHERE
schemaname =
"""
