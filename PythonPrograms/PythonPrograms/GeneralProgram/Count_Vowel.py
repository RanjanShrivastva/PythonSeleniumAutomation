user_ip = str(input("Provide input: "))
# user_ip = str(input("Provide input")).lower()
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
d = {}

for ch in user_ip:
    if ch in vowel:
        d[ch] = d.get(ch, 0)+1
if len(d) == 0:
    print("No vowel Found")
for k, v in d.items():
    print(" Vowel {} occurred {} times".format(k, v))