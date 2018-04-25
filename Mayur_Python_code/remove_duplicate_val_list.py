print("By using predefined function: \n")
val = [12,24,35,24,88,120,155,88,120,155]
duplicate = []
val2 = list(dict.fromkeys(val))
print((val2))
print("Without using predefined function: \n")
for i in val:
	if i not in duplicate:
		duplicate.append(i)

print(duplicate)