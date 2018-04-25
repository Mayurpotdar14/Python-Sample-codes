#Two integer addition and convert them to string and display it.
def integer_to_string():
	x = raw_input("Enter first integer : ")
	y = raw_input("Enter second integer : ")
	z = x + y
	print("Addition of two integers: ", integer_to_string.__doc__)

#iteration and repeat the value, print the first result in one line and next result with old value + new value and goes till end of the loop.  
square = []
for x in range(10):
	square.append(x**2)
	print(square)
print()

#Print the result in one line
cube = [ x**3 for x in range(10)]
print(cube)	
print()


#bellow function using lamda
quad= list (map(lambda x: x**4, range(5)))   
print(quad)

matrix = [[1, 4, 3], [6, 3, 8], [9, 1, 2]] 
transpose = []
for i in range(3):
	transpose.append([row[i] for row in matrix])
print(transpose)
