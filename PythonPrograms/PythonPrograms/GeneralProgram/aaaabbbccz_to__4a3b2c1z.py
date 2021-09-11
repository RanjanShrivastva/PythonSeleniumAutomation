from itertools import groupby


ip = 'aaaabbbcczaaaa'
op = '4a3b2c1z'


# method1
# def transformed_data(ip):
#     output = ''
#     s = sorted(set(ip))
#     for ch in s:
#         output = output + str(ip.count(ch)) + ch
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