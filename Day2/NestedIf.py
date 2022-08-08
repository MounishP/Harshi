"""
Nested If
check one condition within another condition
"""

college = True
calculus = True

if college == True: #True
    print("Harshi is in the college")
    if calculus == True: #True
        print("Harshi attended calculus class")
    else:
        print("Harshi didnt attend calculus class")
else:
    print("Harshi is not in the college")
