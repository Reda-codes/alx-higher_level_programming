#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = str(number)
str = "and is less than 6 and not 0"
if number > 0:
    if int(num[-1:]) == 0:
        print(f"Last digit of {number} is {num[-1:]} and is 0")
    elif int(num[-1:]) <= 5:
        print(f"Last digit of {number} is {num[-1:]} {str}")
    else:
        print(f"Last digit of {number} is {num[-1:]} and is greater than 5")
elif number < 0:
    if int(num[-1:]) == 0:
        print(f"Last digit of {number} is {num[-1:]} and is 0")
    else:
        print(f"Last digit of {number} is -{num[-1:]} {str}")
else:
    print(f"Last digit of {number} is {num[-1:]} and is 0")
