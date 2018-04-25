#6.	Define a function that can accept an integer number as input and print the “It is an even number” if the number is even,
# otherwise print “It is an odd number”.
def statement_print(st):
    if st % 2 == 0:
        print("Integer is even")
    else:
        print('Integer is odd')
val = statement_print(20)
print('------------------------------------------------------------------------------------------------')


#7. and 8.	Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys.
def dict_sq(k):
    d = dict()
    print('Dictionary : ')
    for k in range(1, 20):
        d[k] = k ** 2
    return d
print(dict_sq(20))
print('------------------------------------------------------------------------------------------------')


#9.	Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and
# the values are square of keys. The function should just print the keys only.
#10. Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
def dict_sq():
    d = dict()
    print('Dictionary  Keys and values separated : ')
    for k in range(1, 21):
        d[k] = k ** 2
    print(d.keys())
    print(d.values())
dict_sq()
print('------------------------------------------------------------------------------------------------')


#11.	Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list. Hint: Use list.append() to add values into a list.
# Use [n1:n2] to slice a list (read how to slice, its simple)
def dict_sq(n):
    x = list(map(lambda x: x*x, range(1, n+1)))
    print(x[0:5])
    for i in range(0,5):
        y = (x[i] + x[i+1])
    print('Addition of first five element from list : ',y)
z = dict_sq(20)
print('------------------------------------------------------------------------------------------------')


#12. Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both included).
def square_dict(n):
    d = dict()
    print('Tuples : ')
    for x in range(1, 21):
        d[x] = x ** 2
    return d.items()
print(square_dict(20))
print('------------------------------------------------------------------------------------------------')



#13. With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
# Hint: Use [n1:n2] notation to get a slice from a tuple.
def list_split(lp):
    x = list(map(lambda x: x * x, range(1, lp + 1)))
    print(x[0:5])
    print(x[5:10])
z = list_split(10)
print('------------------------------------------------------------------------------------------------')



def even_odd_tuple(t):
    d = dict()
    print('Even Odd Tuple List : ', end='')

    even_tuple = []
    odd_tuple = []

    for x in range(1, 10):
        d[x] = x ** 2
    print(d)
    for i in range(1, 10):
        if d[i] % 2 == 0:
            even_tuple.append(i)
        else:
            odd_tuple.append(i)

    print('Even Tuples :  ', even_tuple)
    print('Odd Tuples: ', odd_tuple)

    return d.items()
z = even_odd_tuple(10)
print('------------------------------------------------------------------------------------------------')
