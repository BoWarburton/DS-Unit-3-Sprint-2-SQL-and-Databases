
get_characters = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(get_characters).fetchall()
print(len(characters))
print(characters[:5])


print(sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall())
create_character_table = """
CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INTEGER,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
);
"""

# dbname = 'pkyeqwjs'
# user = 'pkyeqwjs'
# password = 'yCST0CUudYye77u_fWs1AJAXufSKUT8A'
# host = 'ruby.db.elephantsql.com'

# pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
# # print(pg_conn)

# pg_curs = pg_conn.cursor()



# print(len(characters))
# print(characters[:5])

# # we now have a list of tuples with all our character data
# # not a pandas df

# # step 2 transform



# show_tables = """
# SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema'
# """

# pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

# pg_curs = pg_conn.cursor()
# # pg_curs.execute(create_chracter_table)
# # pg_conn.commit()

# # pg_curs.execute('SELECT * FROM charactercreator_character LIMIT 5;')
# # print(pg_curs.fetchall())

# print (len(pg_character))
# for character, pg_character in zip(characters, pg_characters):
#     assert character == pg_character