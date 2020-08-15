#!/opt/anaconda3/bin Python
import sqlite3

"""
ANSWER: 10 most expensive items per unit price
1. Cote de Blaye
2. Thuringer Rostbratwurst
3. Mishi Kobe Niku
4. Sir Rodney's Marmalade
5. Carnarvon Tigers
6. Raclette Courdavault
7. Manjimup Dried Apples
8. Tarte au sucre
9. Ipoh Coffee
10. Rossle Sauerkraut
"""

'''
ANSWER average age of employee at time of hiring: 37.2 years old
'''

'''
ANSWER 10 most expensive items and suppliers
1: Côte de Blaye, Aux joyeux ecclésiastiques
2: Thüringer Rostbratwurst, Plutzer Lebensmittelgroßmärkte AG
3: Mishi Kobe Niku, Tokyo Traders
4: Sir Rodney's Marmalade, Specialty Biscuits, Ltd.
5: Carnarvon Tigers, Pavlova, Ltd.
6: Raclette Courdavault, Gai pâturage
7: Manjimup Dried Apples, G'day, Mate
8: Tarte au sucre, Forêts d'érables
9: Ipoh Coffee, Leka Trading
10: Rössle Sauerkraut, Plutzer Lebensmittelgroßmärkte AG
'''

'''
ANSWER largest category by unique products in it: Confections
'''

# Open connection to new blank database file
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# 10 most expensive items
curs.execute('SELECT ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10;')
print(f'\n 10 most expensive products')
product_list = curs.fetchall()
for i in range(len(product_list)):
    print(f'{i + 1}: {product_list[i][0]}')

# Average age of employee at time of hiring
curs.execute('SELECT AVG(HireDate - BirthDate) FROM Employee;')
print(f'\n Average age at time of hiring: {curs.fetchall()[0][0]:.2f}')

# (Stretch) average age of employee at hire by city
average_age_by_city = """
SELECT City, AVG(HireDate - BirthDate)
FROM Employee
GROUP BY City
"""
curs.execute(average_age_by_city)
age_by_city = curs.fetchall()
print('\nAverage age of employee at hire by city')
for city, age in zip(age_by_city, age_by_city):
    print(f'{city[0]} {age[1]}')

# 10 most expensive items and their suppliers
most_expensive_items_and_suppliers = """
SELECT ProductName, CompanyName
FROM Product
JOIN Supplier
ON Product.SupplierId = SupplierId
ORDER BY UnitPrice
DESC
LIMIT 10;
"""
curs.execute(most_expensive_items_and_suppliers)

print(f'\n 10 most expensive with suppliers')
product_supplier_list = curs.fetchall()
for i in range(len(product_supplier_list)):
    print(f'{i + 1}: {product_supplier_list[i][0]}, {product_supplier_list[i][1]}')

# Same as above, but Pythonic looping over a list
print('\n')
print('...printed more Pythonic using zip list')
for product, supplier in zip(product_supplier_list, product_supplier_list):
    print(f'{product[0]}, {supplier[1]}')

print('\n')
print('...printed using enumerate')
for num, product in enumerate(product_supplier_list, start=1):
    print('{}. {}, {}'.format(num, product[0], product[1]))

# Largest category by unique number of products in it
largest_category = """
SELECT c.CategoryName, COUNT(c.CategoryName)
FROM Category c, Product p
WHERE c.Id = p.CategoryId
GROUP BY 1
ORDER BY 2 DESC
;
"""
curs.execute(largest_category)
print(f'\n Largest category by unique products: {curs.fetchall()[0][0]}\n')

# (Stretch) employee with the most territories
most_territories = """
SELECT b.LastName AS Name, COUNT(*) AS Territories
FROM EmployeeTerritory a, Employee b
WHERE a.EmployeeId = b.Id
GROUP BY EmployeeId
ORDER BY Territories DESC LIMIT 1;
"""
curs.execute(most_territories)
employee = curs.fetchall()
# .fetchone()
print(f'\n Employee {employee[0][0]} has most territories ({employee[0][1]})')
