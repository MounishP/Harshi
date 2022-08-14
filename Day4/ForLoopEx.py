"""
range(10) -> 0 to 9
range(1,10)start,stop-1 -> 1 to 9



Difference between For loop and while loop:
For loop runs over a sequence without skipping any iteration in between
While loop runs to achieve the end limit even when it is skipping the iteration
"""
# range(1,11) ->[1,2,3,4,5,6,7,8,9,10]
for i in range(1, 11):  # i=1,2,4,5,6,7,8,9,10
    print(f'9*{i}={9*i}')  #9*10=90
    print("inside for loop")
print("outside for loop")