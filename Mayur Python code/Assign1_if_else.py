y=int(input("Please enter your Age : "))
if y > 0 and y<=21:
	print('You are not allowed to enter the club')
elif y > 22 and y<=50:
	print('You are allowed to enter the club')
else:
	print('Beyond age 50 are not permited in to the club')