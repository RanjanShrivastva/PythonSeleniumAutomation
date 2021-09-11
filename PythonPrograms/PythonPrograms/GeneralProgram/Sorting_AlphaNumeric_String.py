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


sort_alpha_numeric(ip)
