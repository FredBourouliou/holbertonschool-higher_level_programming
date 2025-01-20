#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for number in my_list[::-1]:
        print("{:d}".format(number))
