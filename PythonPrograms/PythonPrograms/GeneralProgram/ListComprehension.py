# List Comprehension
evens = [x for x in range(0, 10) if x % 2 == 0]
print(evens)
odds = [x for x in range(0, 10) if x % 2 != 0]
print(odds)
print(evens+odds)

# Dict Comprehension
dict1 = {i: f"Item {i}" for i in range(1, 6)}
print(dict1)
# Reversed Key-Value pair
dict2 = {value: key for key, value in dict1.items()}
print(dict2)
