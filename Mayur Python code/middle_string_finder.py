user_string = input("Enter the string : ")
print(user_string)
print()

def middle_string(str):
	len1 = 0;
	for char in user_string:
		len1 = len1 + 1
	print(len1)
	
	if (len1 % 2 == 0):
		print("There is no middle word ")
	else:
		mid = int(len1 / 2)
		print(user_string[mid])
	
middle_string(user_string)

