
#Find the common number in two list.
list1=[1,342,75,23,98]
list2=[75,23,98,12,78,10,1]
list3=[]
for i in list1:
	if i in list2:
		list3.append(i)
print list3
