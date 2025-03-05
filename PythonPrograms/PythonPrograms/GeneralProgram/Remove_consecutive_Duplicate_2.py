ip = [1, 2, 2, 3, 4, 4, 5, 1, 2]
i = 0
dupe = False
while i < len(ip)-1:
    if ip[i] == ip[i+1]:
        del ip[i]
        dupe = True
    elif dupe:
        del ip[i]
        dupe = False
    else:
        i += 1
print(ip)