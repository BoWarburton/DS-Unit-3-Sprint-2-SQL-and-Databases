#!/opt/anaconda3/bin Python

# "How was working with MongoDB different from working with PostgreSQL?
# What was easier, and what was harder?"
# Harder: Setup. Curly braces. Learning to love Python dictionaries.
# Easier: no schema. Finding is more like a Google search.

import sqlite3
import pymongo

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()
get_rpg_characters = 'SELECT * FROM charactercreator_character;'
rpg_characters = sl_curs.execute(get_rpg_characters).fetchall()
keys = ('character_id,', 'name', 'level', 'hp', 'level', 'strength',
        'intelligence', 'dexterity', 'wisdom')
password = 'pwd'
dbname = 'dbname'
connection = ('mongodb+srv://AArPK5Hk:' + password +
              '@cluster0.nadgn.gcp.mongodb.net/' + dbname +
              '?retryWrites=true&w=majority')
db = pymongo.MongoClient(connection).rpg_db.characters
db.insert_many(
    [{k: v for k, v in zip(keys, char)} for char in rpg_characters]
)

# print(f'\nDoc:\n{doc}\n')
"mongodb+srv://dbUser:xxxxxxxx@cluster0.jgkc5.mongodb.net" \
"/test?retryWrites=true&w=majority") db = client.test
