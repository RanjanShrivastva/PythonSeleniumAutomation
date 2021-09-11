user_ip = str(input("Provide input"))
# user_ip = str(input("Provide input")).lower()
vowel =['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
d = {}

for ch in user_ip:
    if ch in vowel:
        d[ch] = d.get(ch, 0)+1

for k, v in d.items():
    print("{} occurs {} times".format(k,v))