#!/usr/bin/env Python
import psycopg2

from keys import DB_HOST, DB_NAME, DB_PASS, DB_USER

conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                        password=DB_PASS, host=DB_HOST, port='5432'
)
curs = conn.cursor()


# Write a query for the following questions using James' PostgreSQL instance.
# ***Note*** This instance is part of a live project therefore, we will only
# perform 'Read' from the CRUD acronym - DO NOT CREATE/UPDATE/DELETE ANYTHING <3

# For these questions, the columns needed will be in parentheses.
# To see the column names across all tables, follow the ERD at the link below.
# https://github.com/Lambda-School-Labs/juxta-city-data-ds/blob/repo-cleaning/findurcity/src/database/FindUrCity-Entity_2.pdf


# 1. How many rows are in the reference table?
query1 =  '''
SELECT COUNT(*)
FROM reference;
'''

# 2. How many cities (city_name) are in each state (code)?
query2 =  '''
SELECT
	code,
	COUNT(city_name) n_cities
FROM
	reference
GROUP BY 1
ORDER BY 2;
'''

# 3. Return states (code) and average median_house_values rounded to two decimal places - Order by house value.
# ***HINT - you'll need "ROUND(AVG(median_house_value)::NUMERIC, 2)" in SELECT statement***
query3 =  '''
SELECT
	r.code,
	ROUND(AVG(median_house_value)::NUMERIC, 2)
FROM
	reference r
JOIN
	housing h ON r.id=h.id
GROUP BY 1;
'''

# 4. Return cities (city_name) and states (code) where normalized_heart_disease is at least 0.2.
# ***Order by normalized_heart_disease***
# ***HINT - use a subquery - Alias as 'innerTable'***
query4 =  '''
SELECT
	city_name,
	code,
	normalized_heart_disease
FROM (
	SELECT
		*
	FROM
		reference r
	JOIN
		heart_disease h ON r.id=h.id
	) as innerTable
WHERE normalized_heart_disease >= 0.2
ORDER BY 3;
'''