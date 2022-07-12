679. 24 Game


# King of Backtrack
# remember there are only 9216 different outcome for a given cards
# the division may have residual from the real outcome, so we need set a epsilon
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        TARGET = 24
        EPSILON = 10 ** (-6)
        ADD, MULTI, SUBTR, DIVIDE = 0, 1, 2, 3

        def backtrack(nums):
            if not nums:
                # which is impossible
                return False

            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPSILON

            # select two cards from nums
            # note that for add and multiply, order is unnecessary
            # so we could skip further program when i > j in the light of these two operation
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i == j:
                        continue

                    nextNums = []
                    # if there is number left, add in the nextNums
                    for k, z in enumerate(nums):
                        if k != i and k != j:
                            nextNums.append(z)

                    # make a choice in operations
                    for op in range(4):
                        # if op is add or multiply
                        if op < 2 and i > j:
                            continue   

                        if op == ADD:
                            nextNums.append(x + y)

                        if op == MULTI:
                            nextNums.append(x * y)

                        if op == SUBTR:
                            nextNums.append(x - y)

                        if op == DIVIDE:
                            # y is zero, or very close to zero
                            if abs(y) < EPSILON:
                                continue
                            nextNums.append(x / y)

                        # backtrack
                        if backtrack(nextNums):
                            return True

                        # next operation
                        nextNums.pop()

            # enumerate all possibility, still cannot find a valid answer
            return False

        return backtrack(cards)



