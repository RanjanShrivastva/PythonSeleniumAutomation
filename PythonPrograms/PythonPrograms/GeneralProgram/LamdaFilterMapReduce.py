from functools import reduce

nums = [3, 2, 6, 8, 6, 3, 2, 9]

evens = list(filter(lambda n: n % 2 == 0, nums))    # To select set of numbers from numbers
odds = list(filter(lambda n: n % 2 != 0, nums))
doubles = list(map(lambda n: n*2, nums))   # To perform operation like sum, mul, div, remainder
sums = reduce(lambda a, b: a + b, nums)  # To reduce
print(nums)
print(evens)
print(odds)
print(doubles)
print(sums)

