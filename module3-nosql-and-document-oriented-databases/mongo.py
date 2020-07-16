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

# Step 2 - Loop through character list making Mongo docs

rpg_docs = []
for i in range(len(rpg_characters)):
    doc = {'doc_type': 'rpg_characters',
           'sql_key': rpg_characters[i][0],
           'name': rpg_characters[i][1],
           'level': rpg_characters[i][2],
           'exp': rpg_characters[i][3],
           'hp': rpg_characters[i][4],
           'strength': rpg_characters[i][5],
           'intelligence': rpg_characters[i][6],
           'dexterity': rpg_characters[i][7],
           'wisdom': rpg_characters[i][8]
          }
    rpg_docs.append(doc)

# print(rpg_docs[:5])

# Step 3 - Insert
import pymongo
client = pymongo.MongoClient("mongodb+srv://dbUser:xxxxxxxx@cluster0.jgkc5.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
db.test.insert_many(rpg_docs)