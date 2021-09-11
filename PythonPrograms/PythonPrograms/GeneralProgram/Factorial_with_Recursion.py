def fact(n):
    if n == 0 or n == 1:
    # if n == 1:
        return 1
    return n * fact(n-1)


result = fact(2)
print(result)
