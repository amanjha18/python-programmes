
a=int(input("enter the number"))
b=int(input("enter the number"))
operator=raw_input("enter operator")
def calculator(a,b,operator):
	if operator=="+":
		return(a+b)
	if operator=="-":
		return(a-b)
	if operator=="*":
		return(a*b)
	if operator=="/":
		return(a/b)
z=calculator(a,b,operator)
print z