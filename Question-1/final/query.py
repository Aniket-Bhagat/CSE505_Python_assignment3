#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('database.db')
# cursor = conn.execute("SELECT * from products")
cur = conn.cursor()

cur.execute("SELECT * FROM users  WHERE userId = ? or email = ?", (5,'aniket.bhagat@gmail.com'))

row = cur.fetchone()
print row

# # print "  First Name    Last Name\n---------------------------"
# for i in cursor:
# 	# print ("| {0:10s} | {1:10s} |".format(i[0],i[1]))
# 	print i

# conn.execute('''INSERT INTO "products" VALUES('test4',11,'description4',50,4);''')

# ---------------------------------------------------------------

def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))


# --------------------------------------------------------------------------------------------
# ID=None
# first='Aniket'
# last='Bhagat'
# email='aniket.bhagat@gmail.com'
# password='12345678'
# address1='2/786, XXX Road, opp. ---'
# address2='Near Somithing, some area'
# zipcode='500032'
# city='Hyderabad'
# state='Telangana'
# country='India'
# phoneNo='000000000'

# items = (ID,first,last,email,password,address1,address2,zipcode,city,state,country,phoneNo)
# # print type(items)
# conn.execute('''INSERT INTO users VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''',items)
# # cur.execute('''INSERT INTO "products" VALUES(null,'test5',45,'description5',10,0);''')
# conn.commit()


conn.close()
