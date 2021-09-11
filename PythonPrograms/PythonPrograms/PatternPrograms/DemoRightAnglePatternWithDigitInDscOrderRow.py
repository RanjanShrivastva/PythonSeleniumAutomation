"""
Example to print in the form
5
5, 4
5 4 3
5 4 3 2
5 4 3 2 1
"""
# Code starts here
ip = int(input("Provide a number to print right angle triangle: "))
# Digit in as order
for i in range(ip):
    for j in range(i+1):
        print(str(ip-j), end=' ')
    print()
print('*'*30)

# Alphabet in dictionary order
"""
D
D C
D C B
D C B A
"""
for i in range(ip):
    for j in range(i+1):
        print(chr(64+ip-j), end=' ')
    print()
