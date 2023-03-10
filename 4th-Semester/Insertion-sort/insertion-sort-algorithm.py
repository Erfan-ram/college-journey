# colored text
import sys
RED = "\033[1;31m"
RESET = "\033[0m"
YELLOW = "\033[1;33m"

# Insertion sort is a simple sorting algorithm that works similar to the way you sort
# playing cards in your hands. The arrayay is virtually split into a sorted and
# an unsorted part. Values from the unsorted part are picked and placed at the correct
# position in the sorted part.


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


print(
    f"{RED}Please enter a list of numbers in a row seperating with \'-\' to get sorted{RESET}")
ask = input(f"\t (num-num-num-num)      {YELLOW}UR num:{RESET}  ")

# convert string to list of numbers
test_array = ask.split('-')
test_array = list(map(lambda x: int(x), test_array))

sorted = insertion_sort(test_array)

print("\nsorted numbers :  ")
for i in test_array:
    print(f"{YELLOW}{i}", end=" ")
