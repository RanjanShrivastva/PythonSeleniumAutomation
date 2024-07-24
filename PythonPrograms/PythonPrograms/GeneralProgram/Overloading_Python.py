class Test:
    def __init__(self, *args):
        print('constructors with ', len(args),  'args')
        for i in args:
            print(i)
        print()


t = Test()
t1 = Test(10)
t2 = Test(10, 20)
t3 = Test(10, 20, 30)

# print(t, t1, t2, t3)
