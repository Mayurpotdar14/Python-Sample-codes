from random import *
val= randint(500,1000)
count = 1
trial_range = 20

for i in range(1, 21):
	count = count + 1
	num =int(input("Enter the guessing number :"))
	print()
	if num < 500:
		print("Enter valid range above 100 : ")
	elif num > 1000:
		print("Enter valid range bellow 1000 : ")
	elif num > 500 and num < 1000:
		if num==val:
			print("Match found",num,"=",val)
			print("Total trail count is : ", count)
			break
		elif num > val:
			print("Enter lesser but closer number  ")
		elif num < val:
			print("Enter Grater but closer number  ")

	
	