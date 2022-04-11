30. Substring with Concatenation of All Words


# Considering the number of words is the only substring requirement.
# Sliding window plus word counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        word_len = len(words[0])
        word_num = len(words)
        n = len(s)

        words_counter = Counter(words)
        res = []

        # windows move forward by word_len unit each time, 
        # so for covering all substring, the start point has word_len cases
        for start in range(0, word_len):
            left = start
            right = start
            win_counter = Counter()

            # sliding window begin
            while right <= n - word_len:
                w = s[right:right + word_len]
                right += word_len
                # if w is not included in words, then launch a new window from the next index
                if w not in words_counter:
                    left = right
                    win_counter.clear()
                else:
                    win_counter[w] += 1

                    # Once the count of the new word in win_counter is larger than words_counter, shrinking the windows
                    while win_counter[w] > words_counter[w]:
                        out_w = s[left:left+word_len]
                        left += word_len
                        win_counter[out_w] -= 1

                    if win_counter.total() == word_num:
                        res.append(left)

        return res

