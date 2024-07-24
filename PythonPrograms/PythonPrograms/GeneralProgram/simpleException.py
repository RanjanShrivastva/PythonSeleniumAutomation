num1 = int(input("please enter Numerator: "))
num2 = int(input("Please enter Denominator: "))
try:
    print("{} divide by {} is : {} ".format(num1, num2, num1/num2))
except Exception as e:
    print(e)
finally:
    print(" i will run at any cost")

print("Hello Program completed")
