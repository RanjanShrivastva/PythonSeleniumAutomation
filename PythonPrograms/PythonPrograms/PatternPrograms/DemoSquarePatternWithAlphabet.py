n = int(input("Enter a number to print pattern: "))
for i in range(n):
    print((chr(65)+' ') *n)


for i in range(n):
    for j in range(n):
        print((chr(65+j)+' ') *n)
    print()

for i in range(n):
    for j in range(n):
        print(chr(65+j), end=' ')
    print()