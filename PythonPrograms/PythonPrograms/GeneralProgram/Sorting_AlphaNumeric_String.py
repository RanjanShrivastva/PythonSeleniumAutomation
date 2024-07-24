ip = 'B4A1D3'
op = 'ABD134'
alpha = []
numeric = []


def sort_alpha_numeric(ip):
    for ch in ip:
        if ch.isalpha():
            alpha.append(ch)
        else:
            numeric.append(ch)
    output = "".join(sorted(alpha)+sorted(numeric))
    print(output)


def sort_alpha_numeric_using_comprehension(ip):
    string_list = [ch for ch in ip if ch.isalpha()]
    int_list = [ch for ch in ip if ch.isnumeric()]
    # int_list = [ch for ch in ip if not ch.isalpha()]
    print("".join(sorted(string_list)+sorted(int_list)))


sort_alpha_numeric(ip)
sort_alpha_numeric_using_comprehension(ip)
