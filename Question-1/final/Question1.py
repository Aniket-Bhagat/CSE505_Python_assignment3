#!/usr/bin/env python

import itertools, sqlite3, sys
from getpass import getpass

print '''---------------------------------------------------------------------------
---------------------\033[1mWelcome to Online Shopping System\033[0m---------------------
---------------------------------------------------------------------------'''

class User:
	def __init__(self,ID,name,address,phoneNo,):
		self.ID = ID
		self.name = name
		self.address = address
		self.phoneNo = phoneNo

	def view(self,productList):
		for p in productList:
			prdt = '\033[1;95m'+p[1]+'\033[0m'
			print p[0]+' | '+prdt+' | '+p[2]+' | '+p[3]+' | '+p[5]

	def add(self,ProdId):
		with sqlite3.connect("database.db") as conn:
			cur = conn.cursor()
			cur.execute("SELECT * FROM products WHERE productID = ?", [ProdId])
			row = cur.fetchone()
			if row:
				cur.execute('INSERT INTO "kart" VALUES(?,?)',[self.ID,ProdId])
				cur.execute('UPDATE "products" SET stock = stock-1  WHERE productID = ?',[ProdId])
			else:
				print 'product is out of stock or Wrong ID entered'

	def remove(self,ProdId):
		with sqlite3.connect("database.db") as conn:
			cur = conn.cursor()
			cur.execute("SELECT * FROM kart WHERE userId = ? and productId = ?", [self.ID,ProdId])
			row = cur.fetchone()
			if row:
				cur.execute('DELETE FROM "kart" WHERE userID = ? and productID = ?',[self.ID,ProdId])
				cur.execute('UPDATE "products" SET stock = stock+1  WHERE productID = ?',[ProdId])
			else:
				print 'Product is not in your cart'

	def viewCart(self):
		with sqlite3.connect("database.db") as conn:
			cur = conn.execute("SELECT productId,name,price,categoryId FROM products JOIN kart USING (productId) WHERE userId = ? ", [self.ID])
			rows = cur.fetchall()
			Sum=0
			for i in rows:
				prdt = '\033[1;95m'+i[1]+'\033[0m'
				print i[0],prdt,i[2],i[3]
				Sum=Sum+i[2]
			print 'Total = ' + str(Sum)


	def buy(self):
		pass

	def pay(self):
		pass


class guest:
	def __init__(self, name, productList):
		self.name = name
		self.productList = productList

	def displayProducts(self):
		for p in self.productList:
			prdt = '\033[1;95m'+p[1]+'\033[0m'
			print prdt,'|',p[2],'|',p[3],'|',p[5]

class admin():
	# def __init__(self, u_name, a_pass):
	# 	self.u_name = u_name

		
	def view(self):
		pass

	def add(self):
		pass

	def remove(self):
		pass

	def modify(self):
		pass

	def ship(self):
		pass

	def confirm(self):
		pass


def Register(first,last,email,password,chkpassword,address1,address2,zipcode,city,state,country,phoneNo):
	if password == chkpassword:
		with sqlite3.connect("database.db") as conn:
			cur = conn.cursor()
			cur.execute("SELECT * FROM users  WHERE email = ?", [email])
			row = cur.fetchone()

			if row:
				msg = "e-mail id %s is already registered, Registration failed!"%(email)
			else:
				cur.execute('INSERT INTO "users" VALUES(null,?,?,?,?,?,?,?,?,?,?,?)',[first,last,email,password,address1,address2,zipcode,city,state,country,phoneNo])
				conn.commit()
				print 'Registration Successful!'
	else :
		print 'Password is not matching, Registration failed!'


def Usr_inp():
	for x in itertools.count():
		try:
			print 'Continue as : 1. Guest  2. Existing User  3. Admin  4. Register new User\n0. exit or type\'exit\' or Ctrl + D'
			yield raw_input('Choice number : ')
		
		except EOFError :
			print ''; break

		except KeyboardInterrupt :
			print ''; pass

def main():
	c = sqlite3.connect('database.db')
	cursor = c.execute("SELECT * from products")
	list_of_products = [i for i in cursor]

	for usr_inp in Usr_inp():
		if usr_inp == '1':
			GuestName = raw_input('Guest Name : ')
			Guest = guest(GuestName,list_of_products)
			Guest.displayProducts()
			print 'To Buy products & Registration type \'Register\' or choose \'4\' \n'

		if usr_inp == '2':
			mail = raw_input('Your e-mail Id : ')
			passw = getpass(prompt='Password : ')
			# print passw
			cur = c.cursor()
			cur.execute("SELECT * FROM users WHERE email = ? and password = ?",[mail,passw])
			row = cur.fetchone()
			if row:
				userID=row[0]
				Name = row[1]+' '+row[2]
				Add = row[5:11]
				contN = row[11]
				print '					Welcome ',Name
				done=False
				while done==False:
					print("""					  =======USER MENU=======
					1. Display all available Products
					2. Add Product to cart
					3. Remove Product from cart
					4. View Cart / Buy Now
					5. Payment
					6. Logout
					""")
					try:
						choice= input("Enter Choice : ")
					except:
						choice=''
					U = User(userID,Name,Add,contN)
					if choice==1:
						U.view(list_of_products)
					elif choice==2:
						print 'Give productID line by line and press Enter to confirm.'
						while True:
							prdctId = raw_input()
							if len(prdctId)>0:
								U.add(int(prdctId))
							else:
								break
					elif choice==3:
						print 'Give productID line by line and press Enter to confirm.'
						while True:
							prdctId = raw_input()
							if len(prdctId)>0:
								U.remove(int(prdctId))
							else:
								break
					elif choice==4:
						U.viewCart()
					elif choice==5:
						pass
					elif choice==6:
						print "Successfull logged out\n"
						done=True
					else :
						print "Invalid option"

			else:
				print 'Invalid credentials\nLogin Failed..!'

		if usr_inp == '3':
			ausername = raw_input('Your username : ')
			apassw = getpass(prompt='Password : ')
			cur = c.cursor()
			cur.execute("SELECT * FROM admins WHERE username = ? and password = ?",[ausername,apassw])
			row = cur.fetchone()
			if row:
				print '					login as Administrator : %s' %ausername
				done=False
				while done==False:
					print("""					  =======ADMIN MENU=======
					1. Display all available Stocks of product
					2. Add Product to database
					3. Remove Product from database
					4. View Shipments
					5. Confirmed orders
					6. Logout
					""")
					try:
						choice= input("Enter Choice : ")
					except:
						choice=''
					if choice==1:
						pass
					elif choice==2:
						pass
					elif choice==3:
						pass
					elif choice==4:
						pass
					elif choice==5:
						pass
					elif choice==6:
						print "Successfull logged out\n"
						done=True
					else:
						print 'Invalid Option'
			else:
				print 'Invalid credentials\nLogin Failed..!'

		if usr_inp == '4' or usr_inp == 'Register':
			fname = raw_input('\nFirst Name : ')
			lname = raw_input('Last Name : ')
			mail = raw_input('e-mail ID : ')
			passw = getpass(prompt='Password : ')
			rpassw = getpass(prompt='Retype Password : ')
			add1 = raw_input('Address Line1 : ')
			add2 = raw_input('Address Line2 : ')
			zipc = raw_input('ZipCode : ')
			city = raw_input('City : ')
			state = raw_input('State : ')
			country = raw_input('Country : ')
			contact = raw_input('Mobile No. : ')

			Register(fname,lname,mail,passw,rpassw,add1,add2,zipc,city,state,country,contact)

		if usr_inp == '0' or usr_inp == 'exit':
			print 'Thank You for Visiting..!!'
			break

if __name__ == '__main__':
	main()
