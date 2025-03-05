def first_n_values_generator(num):
    print("*********** Generator using yield **********")
    i = 1
    while i <= num:
        yield i
        i = i+1


num = int(input("Enter a number to generate numbers: "))
g = first_n_values_generator(num)
for x in g:
    print(x)


# example
print("*********** Generator using comprehension **********")
evens = (i for i in range(1, num+1))
# evens = (i for i in range(1, 20) if i % 2 == 0)
# print(type(evens))
for x in evens:
    print(x)
