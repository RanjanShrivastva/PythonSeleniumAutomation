user_ip_1 = str(input('Enter first number to test anagram: '))
user_ip_2 = str(input('Enter first number to test anagram: '))

if sorted(user_ip_1) == sorted(user_ip_2):
    print('{} and {} is anagram'.format(user_ip_1, user_ip_2))
else:
    print('{} and {} is not anagram'.format(user_ip_1, user_ip_2))