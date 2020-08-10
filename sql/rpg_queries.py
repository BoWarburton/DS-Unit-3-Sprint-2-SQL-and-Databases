#!/usr/bin/env Python
import sqlite3

# 1st connect to db
conn = sqlite3.connect('rpg_db.sqlite3')

# 2nd make a cursor
cursor = conn.cursor()

# 3rd execute SQL as Python string
# create_statement = "CREATE TABLE pizza (name varchar(30), size int, pepperoni int, pineapple int);"
# cursor.execute(create_statement)
# insert_statement = "INSERT INTO pizza (name, size, pepperoni, pineapple) VALUES ('ellios', 9, 1, 0);"
# cursor.execute(insert_statement)
# cursor.execute("SELECT * FROM pizza;").fetchall()
# cursor.execute("SELECT count(*) FROM charactercreator_character WHERE character_id >= 100")

# How many total Characters are there?
character_count = "SELECT count(*) FROM charactercreator_character"
print(cursor.execute(character_count)).fetchall()

# How many of each specific subclass?
# count_mages = "SELECT COUNT(*) FROM charactercreator_character, charactercreator_mage WHERE
# SELECT count(*) FROM cleric, fighter, mage, necromancer, thief

# How many total Items?
# SELECT count(*) FROM armory_item

# How many of the Items are weapons? How many are not?
# SELECT count(*) FROM armory_item WHERE join to armory_
# How many Items does each character have? (Return first 20 rows)
# How many Weapons does each character have? (Return first 20 rows)
# On average, how many Items does each Character have?
# On average, how many Weapons does each character have?
#You do not need all the tables - in particular, the account_*, auth_*, django_*, and socialaccount_* tables
#are for the application and do not have the data you need. the charactercreator_* and armory_* tables
#and where you should focus your attention. armory_item and charactercreator_character are the main tables
#for Items and Characters respectively - the other tables are subsets of them by type (i.e. subclasses),
#connected via a key (item_id and character_id).

#You can use the DB Browser or other tools to explore the data and work on your queries if you wish,
#but to complete the assignment you should write a file rpg_queries.py that imports sqlite3
#and programmatically executes and reports results for the above queries.

#Some of these queries are challenging - that's OK!
#You can keep working on them tomorrow as well (we'll visit loading the same data into PostgreSQL).
#It's also OK to figure out the results partially with a query and partially with a bit of logic or math afterwards,
#though doing things purely with SQL is a good goal. Subqueries and aggregation functions may be helpful
#for putting together more complicated queries.
