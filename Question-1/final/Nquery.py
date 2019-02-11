#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.execute('''SELECT productId,name,price,categoryId 
						FROM products
						JOIN kart USING (productId) WHERE userId = 1;''')


for i in cursor:
	print i