user_ip = str(input('please provide a string to reverse: '))

# method-1: using slice method
output_1 = user_ip[::-1]
# print("Reverse  of {} is {}".format(user_ip, output_1))

# method-2 using reversed method
reversed_object = reversed(user_ip)
output_2 = ''
for x in reversed_object:
    output_2 = output_2 + x
# print("Reverse  of {} is {}".format(user_ip, output_2))

# method-3 using list and join
reverse_str = []
for x in user_ip:
    reverse_str.append(x)
output_3 = reverse_str[::-1]
output_3 = "".join(output_3)
print("Reverse  of {} is {}".format(user_ip, output_3))
