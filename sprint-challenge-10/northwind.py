'''
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
'''

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
ANSWER largest category by unique products in it: Condiments
'''

#!/usr/env/bin Python
import sqlite3

# Open connection to new blank database file
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# 10 most expensive items
curs.execute('SELECT ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10;')
print(f'\n 10 most expensive products')
product_list = curs.fetchall()
for i in range(len(product_list)):
    print(f'{i+1}: {product_list[i][0]}')

# print(f'10 most expensive: {curs.fetchall()[0]}')

# Average age of employee at time of hiring
curs.execute('SELECT AVG(HireDate - BirthDate) FROM Employee;')
print(f'\n Average age at time of hiring: {curs.fetchall()[0][0]}')

# (Stretch) average age of employee at hire by city

# 10 most expensive items and their suppliers
curs.execute('SELECT ProductName, CompanyName FROM Product JOIN Supplier ON Product.SupplierId = Supplier.Id ORDER BY UnitPrice DESC LIMIT 10;')
print(f'\n 10 most expensive with suppliers')
product_supplier_list = curs.fetchall()
for i in range(len(product_supplier_list)):
    print(f'{i+1}: {product_supplier_list[i][0]}, {product_supplier_list[i][1]}')

# Pythonic looping over a list
print('\n')
for product, supplier in zip(product_supplier_list, product_supplier_list):
    print(f'{product[0]}, {supplier[1]}')

print('\n')

for num, product in enumerate(product_supplier_list, start=1):
    print('{}. {}, {}'.format(num, product[0], product[1]))

# Largest category by unique number of products in it
largest_category = '''
SELECT c.CategoryName, COUNT(c.CategoryName)
FROM Category c, Product p
WHERE c.Id = p.CategoryId
GROUP BY 1
ORDER BY 2 DESC
;
'''
curs.execute(largest_category)
print(f'\n Largest category by unique products: {curs.fetchall()[0][0]}')