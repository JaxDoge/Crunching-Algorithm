904. Fruit Into Baskets


# Sliding window
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = dict()
        left = right = 0
        n = len(fruits)

        if n < 3:
            return n

        while right < n:
            if fruits[right] in basket:
                basket[fruits[right]] += 1

            else:
                basket[fruits[right]] = 1

            # check the validity
            if len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    basket.pop(fruits[left])
                left += 1

            right += 1

        return right - left
