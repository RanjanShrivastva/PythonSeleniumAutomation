"""
Example to print in the form
1
1, 2
1 2 3
1 2 3 4
"""
# Code starts here
ip = int(input("Provide a number to print right angle triangle: "))
# Digit in as order
for i in range(ip):
    for j in range(i+1):
        print(str(j+1), end=' ')
    print()
print('*'*30)

# Alphabet in dictionary order
"""
A
A B
A B C
A B C D
"""
for i in range(ip):
    for j in range(i+1):
        print(chr(65+j), end=' ')
    print()
