#!/usr/bin/env Python
import sqlite3
import pandas as pd

# 1st connect to db
conn = sqlite3.connect('rpg_db.sqlite3')

# 2nd make a cursor
cursor = conn.cursor()

# 3rd make SQL as Python string
character_count = "SELECT count(*) FROM charactercreator_character"
cleric_count = "SELECT count(*) FROM charactercreator_cleric"
fighter_count = "SELECT count(*) FROM charactercreator_fighter"
mage_count = "SELECT count(*) FROM charactercreator_mage"
necromancer_count = "SELECT count(*) FROM charactercreator_necromancer"
thief_count = "SELECT count(*) FROM charactercreator_thief"
item_count = "SELECT count(*) FROM armory_item"
weapon_count = "SELECT count(*) FROM armory_weapon"
items_carried = "SELECT count(character_id) \
    FROM charactercreator_character_inventory \
    GROUP BY character_id LIMIT(20)"
weapons_carried = "SELECT count(character_id) \
    FROM charactercreator_character_inventory, armory_weapon \
    WHERE item_id = item_ptr_id \
    GROUP BY character_id LIMIT(20)"
items_average = "SELECT AVG(count) \
    FROM \
        (SELECT COUNT(character_id) \
        AS count \
        FROM charactercreator_character_inventory \
        GROUP BY character_id)" 
weapons_average = "SELECT AVG(count) \
    FROM \
        (SELECT COUNT(character_id) \
        AS count \
        FROM charactercreator_character_inventory, armory_weapon \
        WHERE item_id = item_ptr_id \
        GROUP BY character_id)"
# cleric_count = "SELECT count(*) \
#     FROM charactercreator_character, charactercreator_cleric \
#     WHERE character_id = character_ptr_id"

# fighter_count = "SELECT count(*) \
#     FROM charactercreator_character, charactercreator_fighter \
#     WHERE character_id = character_ptr_id"

# mage_count = "SELECT count(*) \
#     FROM charactercreator_character, charactercreator_mage \
#     WHERE character_id = character_ptr_id"

# necromancer_count = "SELECT count(*) \
#     FROM charactercreator_character, charactercreator_necromancer \
#     WHERE character_id = mage_ptr_id"

# thief_count = "SELECT count(*) \
#     FROM charactercreator_character, charactercreator_thief \
#     WHERE character_id = character_ptr_id"

# 4th cursor execute and fetchall
print(f'How many total Characters: {str(cursor.execute(character_count).fetchall()[0][0])}')
# print(f'Type of first element of first element of fetchall is {type(cursor.execute(character_count).fetchall()[0][0])}')
# print(f'Type of fetchall is {type(str(cursor.execute(character_count).fetchall()[0][0])}')
# print(f'Type of cursor.execute is {type(cursor.execute(character_count))}')
print(f'How many of subclass cleric: {str(cursor.execute(cleric_count).fetchall()[0][0])}')
print(f'How many of subclass fighter: {str(cursor.execute(fighter_count).fetchall()[0][0])}')
print(f'How many of subclass mage: {str(cursor.execute(mage_count).fetchall()[0][0])}')
print(f'How many of subclass necromancer: {str(cursor.execute(necromancer_count).fetchall()[0][0])}')
print(f'How many of subclass thief: {str(cursor.execute(thief_count).fetchall()[0][0])}')
print(f'How many total Items: {str(cursor.execute(item_count).fetchall()[0][0])}')
print(f'How many of the Items are weapons: {str(cursor.execute(weapon_count).fetchall()[0][0])}')
# print(f'How many are not? {str(cursor.execute(')
print(f'How many items does each character have (first 20 rows): {cursor.execute(items_carried).fetchall()}')
print(f'How many Weapons does each character have (first 20 rows): {cursor.execute(weapons_carried).fetchall()}')
print(f'On average, how many Items does each Character have? {cursor.execute(items_average).fetchall()}')
print(f'On average, how many Weapons does each Character have? {cursor.execute(weapons_average).fetchall()}')
