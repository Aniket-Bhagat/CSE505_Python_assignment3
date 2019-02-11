#! /usr/bin/env python

import itertools, os, re, argparse, sys

def Usr_inp():
	print """\033[34mThis is PyShell\033[0m
press Ctrl + D to exit or type 'exit'"""
	for x in itertools.count():
		try:
			yield raw_input('\033[1m'+os.getcwd()+'\033[0m'+'$ ')
		
		except EOFError :
			print ''; break

		except KeyboardInterrupt :
			print ''; pass



class Switcher:
	def action(self,argument):
		self.arg = argument
		method = getattr(self, argument[0], lambda: "Invalid command")
		return method()

	def pwd(self):
		return os.getcwd()

	def cd(self):
		try:
			String = self.arg[1]
		except IndexError:
			String = ''
		if String == '' or String=='~':
			os.chdir('/home/')
		else :
			try:
				os.chdir(String)
			except OSError:
				return 'Pyshell: cd: '+String+': No such file or directory'

	def ls(self):
		try:
			String = self.arg[1]
		except IndexError:
			String = ''
		if String == '':
			for i in os.listdir('.'):
				print i
		else :
			try:
				for i in os.listdir(String):
					print i
			except OSError:
				return 'ls: cannot access \''+String+'\': No such file or directory'
	
	def touch(self, time=None):
		try:
			fname=self.arg[1]
			ftime = open(fname, 'a')
			try:
				os.utime(fname, time)
			finally:
				ftime.close()
		except IndexError:
			return 'touch: missing file operand'
	
	def grep(self):
		try:
			args = self.arg
			pattern = args[1]
			regex = re.compile(pattern, re.I)
			try:
				hand = open(args[2])
				for line in hand:
					line = line.rstrip()
				
					i = 0; output = ""; count=0
					result = list(regex.finditer(line))
					for m in regex.finditer(line):
						output += "".join([line[i:m.start()], "\033[1;91m", line[m.start():m.end()], "\033[0m"])
						i = m.end()
						count+=1
						if count == len(result):
							print "".join([output, line[m.end():]])
			except:
				return 'grep: '+args[2]+': No such file or directory'
		except IndexError:
			return 'Usage: grep PATTERN [FILE]'

	def head(self):
		args = self.arg
		head = argparse.ArgumentParser(prog="head")
		head.add_argument("command", help=argparse.SUPPRESS)
		head.add_argument("filename", help="Input file name")
		head.add_argument("-n", dest="NoLines", default=10, metavar='<int>', type=int, help="print first N lines")
	
		def firstNlines(fname,N):
			try:
				with open(fname,'r') as File :
					File = File.read().splitlines()
					i=0
					while (i < N):
						print File[i]
						i+=1
			except IOError :
				print ('IOError: No such file or directory: \'%s\'' % fname)
			
		if len(args)>1:
			try:
				parsed_head = head.parse_args(args)
				firstNlines(parsed_head.filename,parsed_head.NoLines)
			except (IndexError,SystemExit) :
				pass
		else:
			head.print_help()

	def tail(self):
		args = self.arg
		tail = argparse.ArgumentParser(prog='tail')
		tail.add_argument("command", help=argparse.SUPPRESS)
		tail.add_argument("filename", help="Input file name", default='')
		tail.add_argument("-n", dest="NoLines", default=10, metavar='int', type=int, help="print last N lines")

		def lastNlines(fname,N):
			try:
				with open(fname,'r') as File :
					File = File.read().splitlines()
					i=-N
					while (i < 0):
						try:
							print File[i]
						except IndexError:
							pass
						i+=1
			except IOError :
				print ('IOError: No such file or directory: \'%s\'' % fname)
		
		if len(args)>1:
			try:
				parsed_tail = tail.parse_args(args)
				lastNlines(parsed_tail.filename,parsed_tail.NoLines)
			except (IndexError,SystemExit) :
				pass
		else:
			tail.print_help()



def main():
	for usr_inp in Usr_inp():
		arg = usr_inp.split(' ')
		if arg[0] == '':
			pass
		elif arg[0] == 'exit':
			break
		else :
			if Switcher().action(arg) == None :
				pass
			else :
				print Switcher().action(arg)

if __name__ == '__main__':
	main()

