#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        div = 0
        total = 0
        for i in my_list:
            div += i[1]
            total += i[0] * i[1]
        return total/div
    else:
        return 0
