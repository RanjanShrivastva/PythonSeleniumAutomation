# method 1: using map
# s1 = "Ranjan"
# s2 = "Kumar1"
# l1 = list(map(lambda x, y: x+y, s1, s2))
# output = "".join(l1)
# print(output)

# Method 2: when two string has any length
s1 = str(input("Enter string 1: "))
s2 = str(input("Enter string 2: "))
i = j = 0
output = ""
while i < len(s1) or j < len(s2):
    if i < len(s1):
        output += s1[i]
        i += 1
    if j < len(s2):
        output += s2[j]
        j += 1
print(output)




