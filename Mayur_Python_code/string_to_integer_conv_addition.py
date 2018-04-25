l = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 !=0):
        l.append(str(i))

print(','.join(l))

#1.	Define a function that can convert an integer into a string and print it in console.
#2.	Define a function that can convert an integer into a string and print it in console.
#3.	Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
#4.	Define a function that can accept two strings as input and concatenate them and then print it in console.
def printval(s1,s2):
	print(int(s1) + int(s2))
printval("23 ","40")

def printval(In1,In2):
	print(In1 + In2)
printval("Str ","Print")

#5.	Define a function that can accept two strings as input and print the string with maximum length in console.
# If two string have the same length, then the function should print both the string line by line.
def printMAX(s1, s2):
    if(len(s1) > len(s2)):
        print(s1)
    elif(len(s1) < len(s2)):
        print(s2)
    else:
        print(s1)
        print(s2)
printMAX("AC","QSA")