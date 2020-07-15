#!/usr/env/bin Python

# "How was working with MongoDB different from working with PostgreSQL?
# What was easier, and what was harder?"
# Harder: Setup. Curly braces. Learning to love Python dictionaries.
# Easier: no schema. Finding is more like a Google search.

# Step 1 - Extract, getting data out of SQLite3
import sqlite3
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
get_rpg_characters = 'SELECT * FROM charactercreator_character;'
rpg_characters = sl_curs.execute(get_rpg_characters).fetchall()
# print(characters[:10])
# print(len(characters[0]))

# Step 2 - Loop through character list, inserting into Mongo

rpg_doc = {
    'doc_type': 'rpg_character',
    'sql_key': rpg_character[0],
    'name': rpg_character[1],
    'level': rpg_character[2],
    'exp': rpg_character[3],
    'hp': rpg_character[4],
    'strength': rpg_character[5],
    'intelligence': rpg_character[6],
    'dexterity': rpg_character[7],
    'wisdom': rpg_character[8]
}