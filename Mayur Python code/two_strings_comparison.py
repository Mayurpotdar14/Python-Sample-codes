global string1, string2

string1 = input("Enter the first string : ")
string2 = input("Enter the second string : ") 

print(string1)
print(string2)

len1 = 0;
len2 = 0;

def str_cmp(s1, s2):
	for char in string1:
		len1 = len1 + 1
	
	for char in string2:
		len2 = len2 + 1

	if len1>len2:
		print("String 1 is longer in length ", string1)
	elif len2>len1:
		print("string 2 is longer in length ", string2)
	else:
		print("string1 = string2", string1,"=", string2, end = '')

str_cmp(string1,string2)