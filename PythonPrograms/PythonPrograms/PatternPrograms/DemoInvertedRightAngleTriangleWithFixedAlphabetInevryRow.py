"""
Example to print in the form
D D D D
C C C
B B
A
"""
# Code starts here
# Method I
n = int(input("Provide a number to print right angle triangle: "))
for i in range(n):
    for j in range(n-i):
        print(chr(64+n-i), end=' ')
    print()
print('*'*30)
# Method II
for i in range(n):
    for j in range(n-i):
        print(chr(64+n-j), end=' ')
    print()



