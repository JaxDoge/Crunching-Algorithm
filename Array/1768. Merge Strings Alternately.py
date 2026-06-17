1768. Merge Strings Alternately

# Two pointers
# p1 start from the 1 char in word2. Similar to p2
# read p1 first then p2. Append the char to the result list
# if any of the pointer move out of the word string length, skip the reading

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)

        res_list = []

        for i in range(max(len1, len2)):
        	if i < len1:
        		res_list.append(word1[i])

        	if i < len2:
        		res_list.append(word2[i])

        return ''.join(res_list)


