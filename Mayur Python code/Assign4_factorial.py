fact = 1
num = int(input('Enter the number: '))
for x in range(1, num +1):
	fact = fact * x
print("Factorial of ", num, "is ", fact)