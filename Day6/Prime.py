"""
Prime number - a number which is completely divisible by 1 and itself
-> n%m==0 it is not a prime
it will have only 2 factors

1. number
    find the factors
2. count the number of factors
3. check if it is a prime
"""

n = int(input("Enter the number: "))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count = count + 1

if count == 2:
    print("It is a Prime")
else:
    print("It is not a Prime")