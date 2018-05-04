import sys

def divide(x, y):
    try:
        res = x/y
    except ZeroDivisionError:
        print('Zero division error')
    else:
        print('Result is :', res)
    finally:
        print('Executing finally clause')

divide(2,3)