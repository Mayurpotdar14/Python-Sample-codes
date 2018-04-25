import random
import string

f = open('a.txt', 'w')
for i in range(10):
    f.write('String Square : ')
    f.write(str(i**3))
    f.write('\n')
f = open('a.txt', 'r')
content = f.read()
print(content)
f.close()


f = open('a.txt')
f1 = open('b.txt', 'w')
for i in f.read():
    f1.write(i)
f1 = open('b.txt', 'r')
content1 = f1.readlines()
print('\n')
print(content1)
f1.close()
f.close()


