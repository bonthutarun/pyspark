
arr = [5, 10, 15, 20, 25]


largest = arr[0]
second_largest = arr[0]


for element in arr:
    if element > largest:
        largest = element


for element in arr:
    if element > second_largest and element != largest:
        second_largest = element


print(f"Largest element: {largest}")
print(f"Second largest element: {second_largest}")
