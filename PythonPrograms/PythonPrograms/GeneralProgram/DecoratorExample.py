def smart_division(func):
    print(func)

    def test(a, b):
        if b == 0:
            print("we cant divide by 0 enter other denominator except 0")
        else:
            func(a, b)
    return test


@smart_division
def division(a, b):
    print("{} divide by {} is {}".format(a, b, a/b))


division(20, 0)


