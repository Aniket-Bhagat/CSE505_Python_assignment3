Run Script:
		$ python Question2.py

It will run Shell like terminal which includes following shell commands:

--------------------------------------------------------------------------------
Example commands :
--------------------------------------------------------------------------------
pwd
cd .
cd ..
cd /
cd ~
ls .
ls ..
ls /
touch file1
touch test.txt
grep perl test.txt
grep " test.txt
head test.txt
head -n test.txt	(should give proper error)
head -n 5 test.txt
tail test.txt
tail -n test.txt	(should give proper error)
tail -n 5 test.txt
something			(should give proper error)
exit
--------------------------------------------------------------------------------


-------
1. `pwd` (To know Present Working Directory)
-------
	<> simply type 'pwd' and press 'Enter' it will print Current Directory Path


-------
2. `cd` (To change Directory)
-------
	<> 'cd' takes at most one argument
	<> 'cd' + 'Enter' changes directory to /home/
	<> 'cd ~' changes directory to /home/
	<> Also works with '.' , '..' & '/'
	<> If invalid path is passed it prompts error out

-------
3. `ls` (List down contents in directory)
-------
	<> 'ls' takes at most one argument
	<> only 'ls + Enter' list contents in present directory
	<> if you give proper path then gives list of that directory
	<> If invalid path is passed it prompts error out

-------
4. `touch` (changes file timestamps)
-------
	<> only works with first argument  ('$ touch file1 file2' creates only file1)
	<> creates new file if not exists
	<> changes timestamps

	Chech timestamp for 'test.txt' provided in folder using '$ touch test.txt'

-------
5. `grep` (print lines matching a pattern)
-------
	<> Usage: grep PATTERN [FILE]
	<> searches pattern with 'ingnoring case'
	<> prints lines with highlighted pattern match
	<> try :
			$ grep perl test.txt

-------
6. `head` (outputs the first part of files)
-------
	<> usage: head [-h] [-n <int>] filename
	<> optional arguments:
			-h, --help  show this help message and exit
			-n <int>    print first N lines
	<> By default gives first 10 lines of file

-------
7. `tail` (outputs the last part of files)
-------
	<> usage: tail [-h] [-n int] filename
	<> optional arguments:
			-h, --help  show this help message and exit
			-n <int>    print last N lines
	<> By default gives last 10 lines of file

