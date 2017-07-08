import os

a=1

while a<300:
	print "copying"
	print a

	command = "cp box-correct.jpg "+"box-"+str(a)+".jpg"
	print command
	os.system(command)
	a=a+1
