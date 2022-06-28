406. Queue Reconstruction by Height


# immitation
# sort the array on first value descending, thus the numbers of inserted people is always larger or equal to the
# next people
# sort the array on second value ascending to avoid insert the people with larger k at the wrong position
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people = sorted(people, key = lambda x: (-x[0], x[1]))

        for p in people:

            # case one, if the length of res is less or equal to p[1], add the p at the end of res
            # because the rest people is always less or equal to p, and has larger or equal p[1]
            # So we could insert p based on p[1]
            if len(res) <= p[1]:
                res.append(p)
            elif len(res) > p[1]:
                res.insert(p[1], p)

        return res

