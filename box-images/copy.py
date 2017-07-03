import os

a=249

while a<297:
	print "copying"
	print a

	command = "cp box.jpg "+"box-"+str(a)+".jpg"
	print command
	os.system(command)
	a=a+1
