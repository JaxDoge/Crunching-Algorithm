68. Text Justification

# Splits the question in different cases; double pointers
# the last line
# one world line
# other ordinary line

def blank(n: int) -> str:
    return ' ' * n

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        right = 0
        n = len(words)

        while True:
            left = right
            lineSum = 0

            # The words' characters and basic one space sumup cannot larger than the line limitation
            while right < n and lineSum + len(words[right]) + right - left <= maxWidth:
                lineSum += len(words[right])
                right += 1

            # Scenario one
            if right == n:
                left_j = " ".join(words[left:])
                rest_spaces = blank(maxWidth-len(left_j))
                res.append(left_j + rest_spaces)
                break

            # determine the spaces b/w two words
            numWords = right - left
            numSpaces = maxWidth - lineSum

            # Scenario two
            if numWords == 1:
                rest_spaces = blank(maxWidth - len(words[left]))
                res.append(words[left] + rest_spaces)
                continue

            else:
                spaceWidth = numSpaces // (numWords - 1)
                extraSpaces = numSpaces % (numWords - 1)
                part1 = blank(spaceWidth + 1).join(words[left:left + extraSpaces + 1])
                part2 = blank(spaceWidth).join(words[left + extraSpaces + 1:right])
                # Note that there is a space b/w part1 and part2
                res.append(part1 + blank(spaceWidth) + part2)

        return res



