ip = 'a4b3c2'
op = 'aaaabbbcc'


def multiply_with_alpha_with_num(ip):
    output = ''
    for ch in ip:
        if ch.isalpha():
            x = ch
        else:
            d = int(ch)
            output = output + x*d
    print(output)


def multiply_with_alpha_with_num_comprehension(ip):
    intList = sorted([i for i in ip if type(i) is int])
    strList = sorted([i for i in ip if type(i) is str])
    print(intList + strList)



multiply_with_alpha_with_num(ip)
multiply_with_alpha_with_num_comprehension(ip)