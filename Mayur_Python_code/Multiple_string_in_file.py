# import string
# import random
# file1 = open('Multiple_string_in_file.txt', 'w')
# def random_string(size = 10, file1 = string.ascii_letters + string.digits):
#     return ''.join(random.choice(file1)for _ in range(size))
# file1.close()
# result = open('Multiple_string_in_file.txt', 'r')
# print(result)
# random_string()

import string
import random
random.random

file1 = open('Multiple_string_in_file.txt', 'w')



def mult_string(chars=string.ascii_uppercase + string.digits):
    for ip in range(10):
        f1 = ''.join(random.choice(chars) for _ in range(6))
    return f1
file1.close()

file1 = open('Multiple_string_in_file.txt', 'r')
f = file1.readline()
file1.close()

print(mult_string())


