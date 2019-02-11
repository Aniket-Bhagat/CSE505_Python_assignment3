import sqlite3

#Open database
conn = sqlite3.connect('database.db')

#Create table
conn.execute('''DROP TABLE IF EXISTS 'users';''')
conn.execute('''CREATE TABLE users 
		(userId INTEGER PRIMARY KEY autoincrement, 
		firstName TEXT,
		lastName TEXT,
		email TEXT,
		password TEXT,
		address1 TEXT,
		address2 TEXT,
		zipcode TEXT,
		city TEXT,
		state TEXT,
		country TEXT, 
		phone TEXT
		)''')
conn.execute('''INSERT INTO "users" VALUES(null,'user1','foo','user1.foo@mail.com','user12345','user1 address line1','user1 address line2','852450','city1','state1','country1','0025154135');''')
conn.execute('''INSERT INTO "users" VALUES(null,'user2','bar','user2.bar@mail.com','user23456','user2 address line1','user2 address line1','852456','city2','state2','country2','0025121021');''')


conn.execute('''DROP TABLE IF EXISTS 'admins';''')
conn.execute('''CREATE TABLE admins
		(adminId INTEGER PRIMARY KEY,
		username TEXT,
		password TEXT);''')
conn.execute('''INSERT INTO "admins" VALUES(1,'admin1','admin123foo');''')


conn.execute('''DROP TABLE IF EXISTS 'products';''')
conn.execute('''CREATE TABLE products
		(productId INTEGER PRIMARY KEY autoincrement,
		name TEXT,
		price REAL,
		description TEXT,
		stock INTEGER,
		categoryId INTEGER,
		FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
		);''')
conn.execute('''INSERT INTO "products" VALUES(1000,'Product0',45,'description of product0',10,0);''')
conn.execute('''INSERT INTO "products" VALUES(1001,'Product1',28,'description of product1',20,1);''')
conn.execute('''INSERT INTO "products" VALUES(1002,'Product2',82,'description of product2',30,2);''')
conn.execute('''INSERT INTO "products" VALUES(1003,'Product3',64,'description of product3',40,3);''')
conn.execute('''INSERT INTO "products" VALUES(null,'Product4',78,'description of product4',85,8);''')


conn.execute('''DROP TABLE IF EXISTS 'kart';''')
conn.execute('''CREATE TABLE kart
		(userId INTEGER,
		productId INTEGER,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')

conn.execute('''DROP TABLE IF EXISTS 'categories';''')
conn.execute('''CREATE TABLE categories
		(categoryId INTEGER PRIMARY KEY,
		name TEXT
		)''')


conn.close()

