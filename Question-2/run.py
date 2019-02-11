#!/usr/bin/env python
# class Switcher(object):
#     def numbers_to_months(self, argument):
#         """Dispatch method"""
#         method_name = 'month_' + str(argument)
#         # Get the method from 'self'. Default to a lambda.
#         method = getattr(self, method_name, lambda: "Invalid month")
#         # Call the method as we return it
#         return method()
 
#     def month_1(self):
#         return "January"
 
#     def month_2(self):
#         return "February"
 
#     def month_3(self):
#         return "March"
 
# a=Switcher()
# print a.numbers_to_months(1)


# class bcolors:
#    HEADER = '\033[95m'
#    OKBLUE = '\033[94m'
#    OKGREEN = '\033[92m'
#    WARNING = '\033[93m'
#    FAIL = '\033[91m'
#    ENDC = '\033[0m'
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'
#    # print bcolors.WARNING + "Enter name:"  + bcolors.ENDC
#    # storage_select = raw_input()

# text = "Enter name"
# a = raw_input(bcolors.OKGREEN + text + bcolors.ENDC)
# print a


class some:
	def test(self,arg):
		for i in range(1,3):
			suff = 'a'+str(i)
			self.suff = arg[i]
			return self.suff
		# self.a1 = arg[1]
		# self.a2 = arg[2]

	def new(self):
		print self.a1
		print self.a2


x=some()
x.test(['a','b','c'])

x.new()