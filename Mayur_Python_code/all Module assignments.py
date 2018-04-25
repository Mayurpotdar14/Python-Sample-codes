print('-------------------------------------------------------------------------------- ')
#1.	Generate a random float where the value is between 10 and 100 using Python math module
import random
random.random


def rand():
    randval = random.uniform(10, 100)
    print('1. Range 10 to 100 : ',randval)
rand()
print('-------------------------------------------------------------------------------- ')


#2.	Generate a random float where the value is between 5 and 95 using Python math module
import random
random.random


def randval():
    val = random.uniform(5, 95)
    print('2. Range 5 to 95 : ', val)
randval()
print('-------------------------------------------------------------------------------- ')


#3.	Write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
import random
random.random


def rand_even_int():
    val = random.randrange(0, 10, 2)
    print('3. Even Random Range 0 to 10 : ', val)
rand_even_int()
print('-------------------------------------------------------------------------------- ')


#4.	Write a program to output a random number, which is divisible by 5 and 7, between 0 and 100 inclusive using random module and list comprehension.

import random
random.random


def rand_div():
    print('4. Random number which is Divisible by 5 and 7 only: ', random.choice([i for i in range(200) if i % 5 == 0 and i % 7 == 0]))
rand_div()
print('--------------------------------------------------------------------------------------')


#5.	Write a program to generate a list with 5 random numbers between 100 and 200 inclusive
import random
random.random

print('5. Random 5 elements Range: ', random.sample(range(100, 200), 5))
print('--------------------------------------------------------------------------------------')

#6.	Write a program to generate a list with 5 even random numbers between 100 and 200 inclusive
import random
random.random

print('6. Random 5 Even numbers: ', random.sample([i for i in range(100, 200) if i % 2 == 0], 5))
print('--------------------------------------------------------------------------------------')


#7.	Write a program to randomly generate a list with 5 numbers which are divisible by 5 and 7, between 1 and 1000 inclusive.
import random
print('7. Random list of 5 which are divisible by 5 and 7 : ', random.sample([i for i in range(1, 1000) if i % 5 == 0 and i % 7 == 0],5))
print('--------------------------------------------------------------------------------------')


#8.	Write a program to randomly print a integer number between 7 and 15 inclusive.
import random
print('8. Random integer between 7 and 15: ', random.randint(7, 15))
print('--------------------------------------------------------------------------------------')

#9.	& 10. Write a program to shuffle and print the list [3,6,7,8]
import random
from random import shuffle
list1 = [3, 6, 7, 8]
list2 = [3, 6, 7, 8, 10, 4, 5]
shuffle(list1)
shuffle(list2)
print('9. & 10. Shuffle the lists: ', list1, list2)
print('--------------------------------------------------------------------------------------')


#11. Write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24]
li = [5, 6, 77, 45, 22, 12, 24]
li = [i for i in li if i % 2 != 0]
print('11. After removing even from the list: ', li)
print('--------------------------------------------------------------------------------------')

#12.	Using list comprehension, write a program to print the list after removing delete numbers
# which are divisible by 5 and 7 in [1,2,24,12,35,88,70,97,155]
li = [1, 2, 24, 12, 35, 88, 70, 97, 155]
val = list(filter(lambda x: x % 5 != 0 and x % 7 != 0, li))
print('12. List comprehension : ', val)
print('--------------------------------------------------------------------------------------')

#13. Using list comprehension, write a program to print the list after removing the 0th, 2nd , 4th ,6th numbers in [12,24,35,70,88,120,153]
li = [12, 24, 35, 70, 88, 120, 153]
val = [x for (i, x) in enumerate(li) if i % 2 != 0]
print('13. Removing even indexed position value and print the result:  ', val)
print('--------------------------------------------------------------------------------------')

#14. Using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
threeD_array = [[[0 for i in range(3)]for i in range(5)] for i in range(8)]
print('14. 3*5*8 3D array with element 0 :\n')
print(threeD_array)
print('--------------------------------------------------------------------------------------')


#15.	Using list comprehension, please write a program to print the list after removing the 0th, 4th,5th, numbers in [12,24,35,70,88,120,155]
li = [12, 24, 35, 70, 88, 120, 155]
val = [x for (i, x) in enumerate(li) if i not in (0, 4, 5)]
print('15. Remove particular positional elements: ', val)
print('--------------------------------------------------------------------------------------')


#16 By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

li = [12, 24, 35, 70, 88, 120, 155]
val = [x for x in li if x != 24]
print('16. Output: ', val)
print('--------------------------------------------------------------------------------------')


#17.	With a given list [12,24,35,88,120,155,89,155,55],
# write a program to print this list after removing all duplicate values with original order reserved.

def removdup(li):
    newlist = []
    visit = set()
    for i in li:
        if i not in visit:
            visit.add(i)
            newlist.append(i)
    return newlist

li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print('17. Result : ',removdup(li))