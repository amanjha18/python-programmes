	
# gussuing game
for i in range(10):
    user=int(input("enter the number 0 to 10 only"))
    if user==5:
        print "you are gussing right, you won!"
        break
    elif user>5:
    	print "aapne number bada dala"
    elif user<5:
    	print "aapne number chota dala"
    else:
        print "your answer is wrong, enter again"
else:
    print"you attemp 5 times so, you lost the game"