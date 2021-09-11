def smart_division(func):
    def test(a, b):
        if b == 0:
            print("we cant divide by 0 enter other denominator")
        else:
            func(a, b)
    return test


@smart_division
def division(a, b):
    print('Division of {}/{} is {}'.format(a, b, a/b))


division(20, 10)
