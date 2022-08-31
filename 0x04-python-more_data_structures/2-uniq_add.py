#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp = []
    for i in my_list:
        if i not in temp:
            temp.append(i)
    return sum(temp)
