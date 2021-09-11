ip = [1, 2, 3, 3, 2, 2, 4, 5, 5, 6, 5]
# op = [1, 2, 4, 6, 5]
op = []
temp = ip[0]


count = 0
for i in range(1, len(ip)):
    if temp == ip[i]:
        count = count+1
        temp = ip[i]
        ip.remove(temp)

print(ip)