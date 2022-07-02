#!/usr/bin/python3
"""
Py5 Lab 2
"""


def returned_list(first, second):
    return [first, second]


def returned_dict(first, second):
    return {first: second}


def returned_tuple(first, second):
    return first, second


def returned_none(first, second):
    res = first + second


def main():
    first_val = input("Please enter a value: ")
    second_val = input("Please enter another value: ")
    list_res = returned_list(first_val, second_val)
    dict_res = returned_dict(first_val, second_val)
    tup_res = returned_tuple(first_val, second_val)
    none_res = returned_none(first_val, second_val)

    print(f"{list_res} and its type is: {type(list_res)}")
    print(f"{dict_res} and its type is: {type(dict_res)}")
    print(f"{tup_res} and its type is: {type(tup_res)}")
    print(f"{none_res} and its type is: {type(none_res)}")


main()




