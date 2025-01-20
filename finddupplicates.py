arr = [1, 2, 3, 4, 5, 1, 2, 3]
duplicates = []

for i in arr:
    if arr.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)
