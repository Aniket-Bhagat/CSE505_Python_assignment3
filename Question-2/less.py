#!/usr/bin/env python

import argparse

args = ['tail','-n','20','test']

tail = argparse.ArgumentParser(prog='tail')
tail.add_argument("command", help=argparse.SUPPRESS)
tail.add_argument("filename", help="Input file name", default='')
tail.add_argument("-n", dest="NoLines", default=10, metavar='int', type=int, help="print the N lines")

parsed_tail = tail.parse_args(args)


def firstNlines(fname,N):
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

try:
	firstNlines(parsed_tail.filename,parsed_tail.NoLines)
except IndexError:
	pass