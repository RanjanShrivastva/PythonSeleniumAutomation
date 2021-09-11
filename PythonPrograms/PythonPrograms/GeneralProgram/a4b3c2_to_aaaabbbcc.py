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


multiply_with_alpha_with_num(ip)