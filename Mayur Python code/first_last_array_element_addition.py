val = [1,4,9,40,1,3,5,7,12]
print("List is : ",val)
length = len(val)
print("Length of String is: ",length)


mid_val = 1+((len(val) - 1 )// 2)
print("Middle index position is :",mid_val)

for i in range(int(len(val)/2)):
	print(val[i] + val[-i-1]," ", end = '') 
print(val[mid_val - 1])