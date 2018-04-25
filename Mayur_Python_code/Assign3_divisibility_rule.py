
for i in range(10, 99):
	if i % 3 == 0:
		j = i / 5
		if (j % 5) != 0:
			print(i, end=' ')