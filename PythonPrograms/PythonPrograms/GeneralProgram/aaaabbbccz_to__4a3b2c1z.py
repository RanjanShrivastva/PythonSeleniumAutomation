from itertools import groupby


ip = 'aaaabbbcczaaaa'
op = 'a8b3c2z1'


# method1
# def transformed_data(ip):
#     output = ''
#     s = sorted(set(ip))
#     for ch in s:
#         output = output + ch + str(ip.count(ch))
#     print(output)


# method2
def transformed_data(ip):
    output = ''
    gl = groupby(ip)
    for k, g in gl:
        # print('k: {} and g: {}'.format(k, len(list(g))))
        num = str(len(list(g)))
        output = output + str(num) + k
    print(output)


transformed_data(ip)