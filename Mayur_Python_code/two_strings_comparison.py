

string1 = input("Enter the first string : ")
string2 = input("Enter the second string : ") 

print(string1)
print(string2)



def str_cmp(s1, s2):
	len1 = 0;
	len2 = 0;
	for char in string1:
		len1 = len1 + 1
	
	for char in string2:
		len2 = len2 + 1

	if len1>len2:
		print("String 1 = ",string1," is longer in length ")
	elif len2>len1:
		print("String 2 = ",string2," is longer in length ")
	else:
		print("string1 = string2 , ", string1,"=", string2, end = '')

str_cmp(string1,string2)