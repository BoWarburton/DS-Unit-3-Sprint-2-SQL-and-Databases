#!/usr/env/bin Python

import sqlite3
import psycopg2

dbname = 'pkyeqwjs'
user = 'pkyeqwjs'
password = 'xxxxxxxxxx'
host = 'ruby.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()

create_test_table_statement = """
CREATE TABLE IF NOT EXISTS test_table (
   id SERIAL PRIMARY KEY,
   name varchar(40) NOT NULL,
   data JSONB
);
"""
create_character_table = """
CREATE TABLE IF NOT EXISTS charactercreator_character (
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
   schemaname != 'pg_catalog'
AND
   schemaname != 'information_schema';
"""

pg_curs.execute(create_character_table)
pg_conn.commit()

# pg_curs.execute(show_tables)
# print(pg_curs.fetchall())

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

get_characters = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(get_characters).fetchall()
print(len(characters))

characters_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES """ + str(characters[0][1:]) + ";"

