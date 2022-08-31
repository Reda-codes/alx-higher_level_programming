#!/usr/bin/python3
def roman_to_int(roman_string):
    num = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    total = 0
    temp = 0
    for i in roman_string:
        total += num[i] if num[i] <= temp else num[i] - temp * 2
        temp = num[i]
    return total
