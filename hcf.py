num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
list1=[]
list2=[]
for i in range(1,num1+1):
    # print (i)
    if (int(num1)%i)==0:
        list1.append(i)
for j in range(1,num2+1):
    if (int(num2%j)==0):
        list2.append(j)
# print(list1,list2)
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
print max(list3)
