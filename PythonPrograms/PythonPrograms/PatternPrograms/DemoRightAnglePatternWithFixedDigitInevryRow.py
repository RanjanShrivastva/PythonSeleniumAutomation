"""
Example to print in the form
1
2 2
3 3 3
4 4 4
"""
# Code starts here
# Method I
ip = int(input("Provide a number to print right angle triangle: "))
for i in range(ip):
    for j in range(i+1):
        print(str(i+1), end=' ')
    print()
print('*'*30)
# Method II
"""note: row values are not getting change so we can write without nested loop also"""
for i in range(ip):
    print((str(i+1)+" ")*(i+1))



