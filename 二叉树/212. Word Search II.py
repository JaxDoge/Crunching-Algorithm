212. Word Search II


# DFS + trie tree
R = 26

class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.children = [None] * R


class TrieMap:
    def __init__(self):
        self.size = 0
        self.root = None

    # Create / Add / Write / Update
    def put(self, key, val):
        self.root = self.putHelper(self.root, key, val, 0)

    def putHelper(self, node, key, val, idx):
        if not node:
            node = TrieNode()

        if idx == len(key):
            node.val = val
            return node

        c = key[idx]
        cIdx = ord(c) - ord("a")
        node.children[cIdx] = self.putHelper(node.children[cIdx], key, val, idx + 1)
        return node

    # Read / Retrieve

    def getNode(self, node, key):
        p = node
        for i in range(len(key)):
            if not p:
                return None
            c = key[i]
            p = p.children[ord(c) - ord("a")]
        return p

    def get(self, key):
        res = self.getNode(self.root, key)
        if res is None:
            return None

        return res.val

    def containKey(self, key):
        return self.get(key) is not None



class Solution:

    def isValid(self, i, j, m, n):
        return 0 <= i < m and 0 <= j < n

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trieMap = TrieMap()

        for word in words:
            trieMap.put(word, word)

        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()        
        res = []

        def dfs(i, j, p):
            nonlocal trieMap, board, m, n, directions, visited
            # base case
            if p is None:
                return

            # check if (i, j) is in the children of p
            c = board[i][j]
            pc = p.children[ord(c) - ord("a")]
            if pc is None:
                return

            visited.add((i, j))

            # if find a key
            if pc.val:
                res.append(pc.val)
                pc.val = None

            # check four direction
            for dx, dy in directions:
                newi, newj = i + dx, j + dy
                if not self.isValid(newi, newj, m, n):
                    continue
                if (newi, newj) in visited:
                    continue

                dfs(newi, newj, pc)

            visited.remove((i, j))

            # prune tree, if the key is the longest key, pc point to the end node
            # we could launch the delete program
            flag = False
            for tmp in pc.children:
                if tmp is not None:
                    flag = True

            if not flag:
                p.children[ord(c) - ord("a")] = None

            return

        for i in range(m):
            for j in range(n):
                dfs(i, j, trieMap.root, [])

        return res
