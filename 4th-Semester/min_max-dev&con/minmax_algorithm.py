def find_min_max(arr: list, low, high):
    # base case: if there is only one element
    if low == high:
        return arr[low], arr[low]

    # if there are two elements
    elif high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    else:
        mid = (low + high) // 2
        # recursively divide the array into two halves
        min1, max1 = find_min_max(arr, low, mid)
        min2, max2 = find_min_max(arr, mid+1, high)

        # compare the minimum and maximum values of the two halves
        if min1 < min2:
            global_min = min1
        else:
            global_min = min2

        if max1 > max2:
            global_max = max1
        else:
            global_max = max2

    return (global_min, global_max)
