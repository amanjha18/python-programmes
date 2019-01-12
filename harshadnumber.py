def harshad(a):
	for i in range(1,a):
		count = 0
		b=str(i)
		for j in b:
			count = count + int(j)
		if i%count == 0:
			print "harshad "+str(i)
		else:
			print "not harshad "+str(i)

harshad(2000)