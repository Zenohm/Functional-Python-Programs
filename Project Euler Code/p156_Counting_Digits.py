from itertools import accumulate


def count_digits(number,digit):
    count = 0
    for each_digit in list(str(number)):
        if each_digit == str(digit):
            count += 1
    return count

def find_missing_number(list_of_numbers):
    for x in range(len(list_of_numbers)):
        if x != list_of_numbers[x]:
            return x


def f(n,digit):
    f = sum([count_digits(x,digit) for x in range(n+1)])
    return f
