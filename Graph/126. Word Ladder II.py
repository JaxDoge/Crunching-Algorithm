126. Word Ladder II


# BFS
# I do note that the wordID dictionary is unnecessary
# and another virtual vectors set is needed
from collections import deque, defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # Part 1, contruct the graph with tons of virtual vectors
        wordGraph = defaultdict(list)
        virtualSet = set()

        def addEdge(word):
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = '*'
                virtualW = "".join(chars)
                virtualSet.add(virtualW)
                wordGraph[word].append(virtualW)
                wordGraph[virtualW].append(word)
                chars[i] = tmp

        for word in wordList:
            addEdge(word)

        if beginWord not in wordGraph:
            addEdge(beginWord)

        # Badcase
        if endWord not in wordGraph:
            return []

        # Part 2, BFS
        res = []
        queue = deque()
        queue.append([beginWord])
        visited = set()
        breakFlag = False

        while queue:
            subSize = len(queue)
            for _ in range(subSize):
                curPath = queue.popleft()
                curWord = curPath[-1]
                visited.add(curWord)
                # Connected !
                if curWord == endWord:
                    # clear curPath
                    candPath = []
                    for w in curPath:
                        if w not in virtualSet:
                            candPath.append(w)
                    res.append(candPath[:])
                    breakFlag = True
                for v in wordGraph[curWord]:
                    if v not in visited:
                        curPath.append(v)
                        queue.append(curPath[:])
                        curPath.pop()

            if breakFlag:
                break

        return res

