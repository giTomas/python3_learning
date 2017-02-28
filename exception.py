#!/usr/bin/python3

try:
	fh = open('test', 'w')
	fh.write("This is my test file for exception handling!!")
except IOError:
	print()
else:
   print ("Written content in the file successfully")
   fh.close()
