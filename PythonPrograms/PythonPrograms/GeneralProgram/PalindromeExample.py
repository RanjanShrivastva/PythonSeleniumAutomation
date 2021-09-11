user_ip = str(input('Enter a string to check palindrome: '))
if user_ip[::-1] == user_ip:
    print(user_ip, "is palindrome")
else:
    print(user_ip, "is not palindrome")
