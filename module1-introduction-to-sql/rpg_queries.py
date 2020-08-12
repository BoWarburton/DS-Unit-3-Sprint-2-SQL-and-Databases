#!/opt/anaconda3/bin Python

import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
cursor = conn.cursor()

character_count = "SELECT count(*) FROM charactercreator_character"

cleric_count = "SELECT count(*) FROM charactercreator_cleric"
# cleric_count = "SELECT count(*) \
#     FROM charactercreator_character, charactercreator_cleric \
#     WHERE character_id = character_ptr_id"

fighter_count = "SELECT count(*) FROM charactercreator_fighter"
# fighter_count = "SELECT count(*) \
#     FROM charactercreator_character, charactercreator_fighter \
#     WHERE character_id = character_ptr_id"

mage_count = "SELECT count(*) FROM charactercreator_mage"
# mage_count = "SELECT count(*) \
#     FROM charactercreator_character, charactercreator_mage \
#     WHERE character_id = character_ptr_id"

necromancer_count = "SELECT count(*) FROM charactercreator_necromancer"
# necromancer_count = "SELECT count(*) \
#     FROM charactercreator_character, charactercreator_necromancer \
#     WHERE character_id = mage_ptr_id"

thief_count = "SELECT count(*) FROM charactercreator_thief"
# thief_count = "SELECT count(*) \
#     FROM charactercreator_character, charactercreator_thief \
#     WHERE character_id = character_ptr_id"

item_count = "SELECT count(*) FROM armory_item"

weapon_count = "SELECT count(*) FROM armory_weapon"

not_weapon_count = "SELECT count(*) \
    FROM armory_item a \
    LEFT JOIN armory_weapon b \
    ON a.item_id = b.item_ptr_id \
    WHERE b.item_ptr_id IS NULL;"

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

print(f'How many total Characters: '
      f'{str(cursor.execute(character_count).fetchall()[0][0])}')
print(f'How many of subclass cleric: '
      f'{str(cursor.execute(cleric_count).fetchall()[0][0])}')
print(f'How many of subclass fighter: '
      f'{str(cursor.execute(fighter_count).fetchall()[0][0])}')
print(f'How many of subclass mage: '
      f'{str(cursor.execute(mage_count).fetchall()[0][0])}')
print(f'How many of subclass necromancer: '
      f'{str(cursor.execute(necromancer_count).fetchall()[0][0])}')
print(f'How many of subclass thief: '
      f'{str(cursor.execute(thief_count).fetchall()[0][0])}')
print(f'How many total Items: '
      f'{str(cursor.execute(item_count).fetchall()[0][0])}')
print(f'How many of the Items are weapons: '
      f'{str(cursor.execute(weapon_count).fetchall()[0][0])}')
print(f'How many are not: '
      f'{str(cursor.execute(not_weapon_count).fetchall()[0][0])}')
print(f'How many items does each character have (first 20 rows): '
      f'{cursor.execute(items_carried).fetchall()}')
print(f'How many Weapons does each character have (first 20 rows): '
      f'{cursor.execute(weapons_carried).fetchall()}')
print(f'On average, how many Items does each Character have? '
      f'{cursor.execute(items_average).fetchall()}')
print(f'On average, how many Weapons does each Character have? '
      f'{cursor.execute(weapons_average).fetchall()}')
