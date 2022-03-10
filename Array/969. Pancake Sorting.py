#  recursion
#  find the largest number and move it to the right most with pancake flip
#  flip twice in one recursion

class Solution:
    def __init__(self):
        self.res = list()

    def pancakeSort(self, arr: List[int]) -> List[int]:
        self.sort_array(arr, len(arr))
        return self.res

    def sort_array(self, array, end):
        # base case
        if end == 1:
            return

        # find the index of max integer within range
        max_one = 0
        max_index = 0
        for i in range(end):
            if array[i] > max_one:
                max_index = i
                max_one = array[i]

        #  reverse 0 to max_index. put the largest integer on the top
        self.reverser(array, 0, max_index)
        self.res.append(max_index + 1)  # the number of reversed integer is max_index + 1
        #  reverse 0 to end. put the largest integer at the bottom
        self.reverser(array, 0, end-1)
        self.res.append(end)
        #  recursion for the rest element
        self.sort_array(array, end - 1)

    def reverser(self, array, i, j):
        while i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1


