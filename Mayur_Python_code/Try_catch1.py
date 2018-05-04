import sys

try:
    with open('hello.txt') as f:
        #f = open('hello.txt', 'r')
        s = f.readlines()
        i = len(s)
        print(s, '\n')
        print(i)
except OSError as err:
        print('OS Error: {0}'.format(err))
except ValueError as Verr:
        print('Could not convert the data in to an integer')
except:
        print('Unexpected Error :', sys.exc_info()[0])
        raise