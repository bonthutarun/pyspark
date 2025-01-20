
arr = [5, 10, 15, 20, 25]


large = arr[0]
small = arr[0]


for element in arr:
    if element > large:
        large = element
    if element < small:
        small = element

print(f"Largest: {large}")
print(f"Smallest: {small}")