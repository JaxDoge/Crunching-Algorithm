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




# Python3 program for building suffix
# array of a given text
 
# Class to store information of a suffix
class suffix:
     
    def __init__(self):
         
        self.index = 0
        self.rank = [0, 0]
 
# This is the main function that takes a
# string 'txt' of size n as an argument,
# builds and return the suffix array for
# the given string
def buildSuffixArray(txt, n):
     
    # A structure to store suffixes
    # and their indexes
    suffixes = [suffix() for _ in range(n)]
 
    # Store suffixes and their indexes in
    # an array of structures. The structure
    # is needed to sort the suffixes alphabetically
    # and maintain their old indexes while sorting
    for i in range(n):
        suffixes[i].index = i
        suffixes[i].rank[0] = (ord(txt[i]) -
                               ord("a"))
        suffixes[i].rank[1] = (ord(txt[i + 1]) -
                        ord("a")) if ((i + 1) < n) else -1
 
    # Sort the suffixes according to the rank
    # and next rank
    suffixes = sorted(
        suffixes, key = lambda x: (
            x.rank[0], x.rank[1]))
 
    # At this point, all suffixes are sorted
    # according to first 2 characters.  Let
    # us sort suffixes according to first 4
    # characters, then first 8 and so on
    ind = [0] * n  # This array is needed to get the
                   # position in suffixes[] from original
                   # index.This mapping is needed to get
                   # next suffix.
    k = 4
    while (k < 2 * n):
         
        # Assigning rank and index
        # values to first suffix
        rank = 0
        prev_rank = suffixes[0].rank[0]
        suffixes[0].rank[0] = rank
        ind[suffixes[0].index] = 0
 
        # Assigning rank to suffixes
        for i in range(1, n):
             
            # If first rank and next ranks are
            # same as that of previous suffix in
            # array, assign the same new rank to
            # this suffix
            if (suffixes[i].rank[0] == prev_rank and
                suffixes[i].rank[1] == suffixes[i - 1].rank[1]):
                prev_rank = suffixes[i].rank[0]
                suffixes[i].rank[0] = rank
                 
            # Otherwise increment rank and assign   
            else: 
                prev_rank = suffixes[i].rank[0]
                rank += 1
                suffixes[i].rank[0] = rank
            ind[suffixes[i].index] = i
 
        # Assign next rank to every suffix
        for i in range(n):
            nextindex = suffixes[i].index + k // 2
            suffixes[i].rank[1] = suffixes[ind[nextindex]].rank[0] \
                if (nextindex < n) else -1
 
        # Sort the suffixes according to
        # first k characters
        suffixes = sorted(
            suffixes, key = lambda x: (
                x.rank[0], x.rank[1]))
 
        k *= 2
 
    # Store indexes of all sorted
    # suffixes in the suffix array
    suffixArr = [0] * n
     
    for i in range(n):
        suffixArr[i] = suffixes[i].index
 
    # Return the suffix array
    return suffixArr
 

# imporve sort to radix sort
# Note that the rank have to start from 0 not -1
def countingSort(array, maxN, rk):
    size = len(array)
    res = [suffix()] * size
    count = [0] * (maxN + 1)

    for num in array:
        count[num.rank[rk]] += 1

    for i in range(1, maxN+1):
        count[i] += count[i - 1]

    for i in range(size - 1, -1, -1):
        curN = array[i]
        cum = count[curN.rank[rk]]
        res[cum - 1] = curN
        count[curN.rank[rk]] -= 1

    for i in range(size):
        array[i] = res[i]

    return



def radixSort(array):
    # sort rank1 then sort rank0
    maxRank = 26
    countingSort(array, maxRank, 1)
    countingSort(array, maxRank, 0)
    return


class suffix:
     
    def __init__(self):
         
        self.index = 0
        self.rank = [0, 0]


def buildSuffixArray(txt):
    n = len(txt)

    suffixes = [suffix() for _ in range(n)]
 
    # Initialize suffixes array
    for i in range(n):
        suffixes[i].index = i
        suffixes[i].rank[0] = (ord(txt[i]) -
                               ord("a") + 1)
        suffixes[i].rank[1] = (ord(txt[i + 1]) -
                        ord("a") + 1) if ((i + 1) < n) else 0

    radixSort(suffixes)
    idxToPos = [0] * n

    # first 2 characters is sorted, then it is first 4 need be sorted, then 8 and so on
    k = 2  # k is the sorted length, which cannot exceed n
    while k < n:
        # re-assign rank 0, and store position in idxToPos to re-assign rank1
        rank = 1
        previousRk = suffixes[0].rank[0]
        suffixes[0].rank[0] = rank
        idxToPos[suffixes[0].index] = 0

        for i in range(1, n):
            # same rank as before
            if (suffixes[i].rank[0], suffixes[i].rank[1]) == (previousRk, suffixes[i - 1].rank[1]):
                previousRk = suffixes[i].rank[0]
                suffixes[i].rank[0] = rank
            else:
                rank += 1
                previousRk = suffixes[i].rank[0]
                suffixes[i].rank[0] = rank

            idxToPos[suffixes[i].index] = i
        
        # re-assign rank1
        for i in range(n):
            nextIdx = suffixes[i].index + k
            suffixes[i].rank[1] = suffixes[idxToPos[nextIdx]].rank[0] if nextIdx < n else 0

        radixSort(suffixes)
        k *= 2

    sa = [sf.index for sf in suffixes]

    return sa




# A utility function to print an array
# of given size
def printArr(arr, n):
     
    for i in range(n):
        print(arr[i], end = " ")
         
    print()
 
# Driver code
if __name__ == "__main__":
     
    txt = "banana"
    n = len(txt)
     
    suffixArr = buildSuffixArray(txt, n)
     
    print("Following is suffix array for", txt)
     
    printArr(suffixArr, n)
 
