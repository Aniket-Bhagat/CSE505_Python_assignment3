#!/usr/bin/env python

# args = ['head','test']
args = ['head','-f','5','test']


def firstNlines(fname,N=10):
	try:
		with open(fname,'r') as File :
			File = File.read().splitlines()
			i=0
			while (i < N):
				print File[i]
				i+=1
	except IOError :
		print ('IOError: No such file or directory: \'%s\'' % fname)

if '-n' in args :
	idx = args.index('-n')
	args.pop(idx)
	n = int(args.pop(idx))

	try:
		firstNlines(args[1],N=n)
	except IndexError:
		pass

else:
	firstNlines(args[1])

##############################################################################
##############################################################################

# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# from argparse import ArgumentParser

# parser = ArgumentParser()

# # Add more options if you like
# parser.add_argument("filename")
# parser.add_argument("-n", dest="NoOfLines", default=10, metavar='N', type=int, help="print the N lines")
# parser.add_argument("-f", "--file", dest="myFilenameVariable", help="write report to FILE", metavar="FILE")
# # parser.add_argument("-q", "--quiet", action="store_false", dest="verbose", default=True, help="don't print status messages to stdout")

# args = parser.parse_args(['-f','just_give','test'])

# print(args)


##############################################################################
##############################################################################

#!/usr/bin/env python
# import argparse

# argparser = argparse.ArgumentParser()
# argparser.add_argument("--file", required=True, help="Video file to upload")
# argparser.add_argument("--title", help="Video title", default="Test Title")
# argparser.add_argument("--description", help="Video description",default="Test Description")
# argparser.add_argument("--category", default="22",help="Numeric video category. " + "See https://developers.google.com/youtube/v3/docs/videoCategories/list")
# argparser.add_argument("--keywords", help="Video keywords, comma separated", default="")
# VALID_PRIVACY_STATUSES = ("private","public")
# argparser.add_argument("--privacyStatus", choices=VALID_PRIVACY_STATUSES,
#     default=VALID_PRIVACY_STATUSES[0], help="Video privacy status.")

# #pass in any positional or required variables.. as strings in a list
# #which corresponds to sys.argv[1:].  Not a string => arcane errors.
# args = argparser.parse_args(["--file", "myfile.avi"])

# #you can populate other optional parameters, not just positionals/required
# #args = argparser.parse_args(["--file", "myfile.avi", "--title", "my title"])


# print vars(args)

# #modify them as you see fit, but no more validation is taking place
# #so best to use parse_args.
# args.privacyStatus = "some status not in choices - already parsed"
# args.category = 42

# print vars(args)

# #proceed as before, the system doesn't care if it came from the command line or not
# # youtube = get_authenticated_service(args)    
