while z:=input("Число:\n"):
	if z.isdigit():
		if z[-1]=="1"and("0"+z)[-2]!="1":print(z,"пук")
		elif("0"+z)[-2]=="1"or(z[-1]in"056789"and("0"+z)[-2]in"234567890"):print(z,"пуков")
		else:print(z,"пука")