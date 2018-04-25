
def reverse_number(num):

    rev: int = 0
    while num > 0:
        if 0 < num < 10000:
            reminder = num % 10
            rev = (rev * 10) + reminder
            num = num // 10
        else:
            break
    return rev
print(reverse_number(1928))


