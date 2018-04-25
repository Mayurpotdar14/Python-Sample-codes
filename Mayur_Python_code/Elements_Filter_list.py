
#14.	Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
def element_filter(key):
    d = dict()
    eve_sort_list = []
    for x in range(1, 20):
        d[x] = x
    for i in range(1, 20):
        if d[i] % 2 == 0:
            eve_sort_list.append(i)
        else:
            pass
    print('Even Tuples :  ', eve_sort_list)
    return d.items()
z = element_filter(20)

print('---------------------------------------------------------------------------------------------------------------------')

#15.	Write a program which can filter even numbers in a list by using function. The list is [1,2,3,4,5,6,7,8,9,10].
# Hint: Use filter() to filter some elements in a list. Use lambda to define anonymous function.

def list_filter(val):
    num_list = range(5, 30)
    print(num_list)
    even_num = list(filter(lambda x: x % 2, num_list))
    print(even_num)
    return even_num
a = list_filter(25)
print('---------------------------------------------------------------------------------------------------------------------')

#16. Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
# Hint: Use map() to generate a list. Use lambda to define anonymous functions.

li = [1,2,3,4,5,6,7,8,9,10]
num = list(map(lambda x: x**2, li))
print(num)
print('---------------------------------------------------------------------------------------------------------------------')

#17. Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
li = [1,2,3,4,5,6,7,8,9,10]
evennum = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, li)))
print('Map() and Filter() function: ')
print(evennum)
print('---------------------------------------------------------------------------------------------------------------------')

#18. Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

squaredNumbers = map(lambda x: x**2, range(1,21))
print(squaredNumbers)
print('---------------------------------------------------------------------------------------------------------------------')
