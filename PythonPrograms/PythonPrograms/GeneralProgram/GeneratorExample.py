def first_n_values_generator(num):
    i = 1
    while i <= num:
        yield i
        i = i+1


num = int(input("Enter a number to generate numbers: "))
g = first_n_values_generator(num)
for x in g:
    print(x)
