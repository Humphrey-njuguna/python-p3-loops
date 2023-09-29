#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass

def square_integers(int_list):
    # code goes here!
    pass

def fizzbuzz():
    # code goes here!
    pass
def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")



def square_integers(integer_list):
    squared_list = [x ** 2 for x in integer_list]
    return squared_list


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


