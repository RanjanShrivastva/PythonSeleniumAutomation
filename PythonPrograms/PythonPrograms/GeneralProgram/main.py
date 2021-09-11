# if __name__ == '__main__':

def reverse_string(user_ip):
    # method 1
    # print("Original string is : {} and reversed string is : {}".format(user_ip, user_ip[::-1]))

    # method 2
    # rev_str = reversed(user_ip)
    # final_str = "".join(rev_str)
    # print("Original string is : {} and reversed string is : {}".format(user_ip, final_str))

    # method 3
    # output = ''
    # i = len(user_ip)-1
    # while i >= 0:
    #     output = output + user_ip[i]
    #     i -= 1
    # print("Original string is : {} and reversed string is : {}".format(user_ip, output))

    # # method 4 : for word
    # split = user_ip.split(" ")
    # split1 = split[::-1]
    # output = " ".join(split1)
    # print("Original string is : {} and reversed string is : {}".format(user_ip, output))

    # Method 05 : reversed each word
    l1 = user_ip.split(" ")
    l2 = []
    for word in l1:
        l2.append(word[::-1])
    output = " ".join(l2)
    print(output)




user_ip = str(input("Please enter a string: "))
reverse_string(user_ip)
