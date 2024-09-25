#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i >= 1:
       print(i)
       i -= 1
    print("Happy New Year!")


def square_integers(int_list):
    # code goes here!
    squared = [x ** 2 for x in int_list]
    return squared
    

def fizzbuzz():
    # code goes here!
   for num in range(1,101):     
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
       print(num)
