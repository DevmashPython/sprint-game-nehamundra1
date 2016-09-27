import msvcrt
import time
import sys

step1=5
count1=0
step2=5
count2=0
step3=5
count3=0

start_time=time.time()
print "enter a key"
while(1):
	key1=msvcrt.getch()
	if key1=='\xe0':
		key1=msvcrt.getch()
		if key1=='M':
			count1=count1+1
			print "-->",
			if count1==step1:
				print "\tenter down key"
				break
		else:
			print "oops! wrong key!!"
			sys.exit()
while(1):
	key2=msvcrt.getch()
	if key2=='\xe0':
		key2=msvcrt.getch()
		if key2=='P':
			count2=count2+1
			print "\t\t\t|\n",
			if count2==step2:
				print "\tenter forward key",
				break
		else:
			print "oops!wrong key!!"
			sys.exit()
while(1):
	i=1
	key3=msvcrt.getch()
	if key3=='\xe0':
		key3=msvcrt.getch()
		if key3=='M':
			count3=count3+1
			i=i+1
			print i*" ",
			print "-->",
			if count3==step3:
				print "ended"
				break
		else:
			print "oops!wrong key!!"
			sys.exit()
tym=time.time()-start_time
print "time taken=",str(tym)
print "you made it!!"
