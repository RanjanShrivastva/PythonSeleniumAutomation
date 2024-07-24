

def smart_division(func):
    def test(a, b):
        if b == 0:
            print("Can't divide when Denominator is 0")
        else:
            func(a, b)
    return test


@smart_division
def division(a, b):
    print("{} / {} is ".format(a, b), a/b)


division(10, 0)