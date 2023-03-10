# Insertion sort is a simple sorting algorithm that works similar to the way you sort
# playing cards in your hands. The arrayay is virtually split into a sorted and
# an unsorted part. Values from the unsorted part are picked and placed at the correct
# position in the sorted part.


# Python program to implement Insertion Sort
def insertion_sort(array):
    lenght = len(array)

    for step in range(1, lenght):
        key = array[step]
        j = step-1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array


print("Please enter a list of numbers in a row seperating with \'-\' to get sorted")
ask = input("\t\t\t e.g: 15-20-2-3-6  :    ")

# convert string to list of numbers
test_array = ask.split('-')
test_array = list(map(lambda x: int(x), test_array))

sorted = insertion_sort(test_array)

for i in test_array:
    print(f"{i}", end=" ")
