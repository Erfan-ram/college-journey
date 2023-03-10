# Insertion sort is a simple sorting algorithm that works similar to the way you sort
# playing cards in your hands. The arrayay is virtually split into a sorted and
# an unsorted part. Values from the unsorted part are picked and placed at the correct
# position in the sorted part.


# Python program to implement Insertion Sort
def insertion_sort(array):
    lenght = len(array)

    for i in range(1, lenght):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    return array


test_array = insertion_sort([50, 26, 25, 3, 5, 9])

for i in test_array:
    print(f"{i}",end=" ")
