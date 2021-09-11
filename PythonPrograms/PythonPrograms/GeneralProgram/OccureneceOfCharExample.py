user_ip = str(input("provide string to find char occurrence: "))
dict ={}
for ch in user_ip:
    dict[ch] = dict.get(ch, 0)+1
for key, val in sorted(dict.items()):
    print('{} occurred {} times'.format(key, val))
