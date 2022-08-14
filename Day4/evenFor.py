"""
print even numbers from 1 to 10
1. range(1,11)
2. find even(When a number is divided by 2 and the remainder
is 0, then that number is a even number)
3. print number if even
"""

for i in range(1, 11):
    if i % 2 == 0:
        print(i, " is even")
