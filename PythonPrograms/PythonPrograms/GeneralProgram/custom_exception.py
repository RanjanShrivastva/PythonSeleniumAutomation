class BalanceException(Exception):
    pass


def check_balance():
    money = 10000
    withdraw = 200000
    try:
        balance = money-withdraw
        if balance <= 2000:
            raise BalanceException("Insufficient Balance")
        print(balance)
    except BalanceException as be:
        print(be)


check_balance()