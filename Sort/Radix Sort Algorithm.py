Radix Sort Algorithm



# Let's start from counting sort. Note that the element must be non-negative integer

def countingSort(array):
    size = len(array)
    res = [0] * size
    maxNum = max(array)

    # Initialize count array
    count = [0] * (maxNum + 1)

    # Store the count of each integer
    for num in array:
        count[num] += 1

    # Store the cummulative count
    for i in range(1, maxNum + 1):
        count[i] += count[i - 1]

    # Place each number in original array in correct position based on count array
    # Note that we need loop from end in order to keep it stable(Same integer maintain their relative order)
    for i in range(size - 1, -1, -1):
        cur = array[i]
        cum = count[cur]
        res[cum - 1] = cur
        count[cur] -= 1

    # Destructive method
    for i in range(size):
        array[i] = res[i]

    return

data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)


# Working of Radix Sort


# remode counting sort for sorting elements in the basis of significant places

def countingSort(array, place):
    size = len(array)
    res = [0] * size
    count = [0] * 10   # range between 0~9

    for num in array:
        index = (num // place) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(size - 1, -1, -1):
        cur = (array[i] // place) % 10
        cum = count[cur]
        res[cum - 1] = array[i]
        count[cur] -= 1

    for i in range(size):
        array[i] = res[i]

    return


def radixSort(array):
    maxValue = max(array)

    place = 1
    while maxValue // place > 0:
        countingSort(array, place)
        place *= 10

    return

data = [121, 432, 564, 23, 1, 45, 788]
radixSort(data)
print(data)    



