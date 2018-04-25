quad = list (map(lambda x: x, range(30)))   
print(quad)
print()
print("Odd integers: ")
def del_even(q):
	for k in range(2, len(q)):
		if k % 2 == 0:
			continue
		print(k," ",end ='')

print()
del_even(quad)