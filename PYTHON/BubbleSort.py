# Bubble Sort
# Simple sorting algorithm, swaps adjacent elements if they are not in the correct order
# Time complexity: O(N^2) -> worst case | O(N) -> best case

def bubbleSort(array: list, size: int):
    # iterate over all elements in array
    for n in range(size):
        # last i elements are sorted
        for m in range(0, size-n-1):

            # if element is greater than next element
            if array[m] > array[m+1]:
                # swap elements
                array[m], array[m+1] = array[m+1], array[m]


data = [-2, 45, 0, 11, -9]
size = len(data)
bubbleSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
