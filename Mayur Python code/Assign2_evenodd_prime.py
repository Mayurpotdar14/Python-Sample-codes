num = int(input('Enter the two digit number: '))
for x in range(num):
	print(x)


print("----------------------------------------------------------------------------------")
print("All prime number between 2 to", num)
for i in range(2,num):
	for j in range(2,i):
		if i % j == 0:
			break
	else:
		print(i)

print("----------------------------------------------------------------------------------")

print('Even and Odd number between 2 to ', num)
for k in range(2,num):
	if k % 2 ==0:
		print(k, "is Even number ")
		continue
print("----------------------------------------------------------------------------------")
for k in range(2,num):
	if k % 2 ==0:
		continue
	print(k, "is Odd number")
print("----------------------------------------------------------------------------------")
