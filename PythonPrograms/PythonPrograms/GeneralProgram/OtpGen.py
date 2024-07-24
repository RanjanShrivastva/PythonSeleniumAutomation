import random as r
import string


# function for otp generation
def otp_gen(length):
    otp = ""
    for i in range(length):
        # otp += str(r.randint(1, 9))  # This is for string
        otp += r.choice(string.digits)  # Only numeric otp
        # otp += r.choice(string.ascii_lowercase + string.ascii_uppercase+string.digits + string.punctuation)
        # otp += r.choice(string.ascii_lowercase + string.ascii_uppercase)
    print("Your One Time Password is : ", otp)


otp_gen(6)
