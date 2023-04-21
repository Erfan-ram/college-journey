def sequential_search(arr: list, element):

    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

# test
ex1 = [9, 70, 50, 63, 1, 23, 37]
ex2 = [9, 70, 50, 63, 1, 23, 37, 30, 99, 55, 63]

element = 30
result1 = sequential_search(ex1, element)
result2 = sequential_search(ex2, element)

if result1 != -1:
    print(f"Element found n first list at at index {result1}")
else:
    print("Element not found in first list")
    
if result2 != -1:
    print(f"Element found on second list at index {result2}")
else:
    print("Element not found in second list")