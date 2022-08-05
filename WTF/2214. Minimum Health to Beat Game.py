2214. Minimum Health to Beat Game


# ???
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        allDMG = sum(damage)
        maxDMG = max(damage)

        realBlock = min(maxDMG, armor)

        return allDMG - realBlock + 1
        