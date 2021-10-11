class P:
    y = 20

    def property(self):
        print('cash, land, property')

    def marry(self):
        print("sunita")
        x = 10
        return x


class C(P):
    def marry(self):
        print('namita')
        x = super().marry()
        print(x)


c = C()
c.marry()
