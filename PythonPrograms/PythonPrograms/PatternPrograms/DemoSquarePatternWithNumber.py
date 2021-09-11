user_ip = int(input("enter a number to print square pattern: "))
for i in range(user_ip):
    print("* " *user_ip)

print('*'*10)
for i in range(user_ip):
    print((str(user_ip) + ' ') *user_ip)

print('*'*10)
for i in range(user_ip):
    print((str(i+1) + ' ') *user_ip)

