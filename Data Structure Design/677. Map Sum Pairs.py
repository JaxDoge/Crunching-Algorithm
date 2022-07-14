677. Map Sum Pairs



# Trie Tree
R = 26

class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.children = [None] * R

class TrieMap:
    def __init__(self):
        self.size = 0
        self.root = TrieNode()

    # create / update
    def put(self, key, val):
        p = self.root
        for c in key:
            cIdx = ord(c) - ord("a")
            if p.children[cIdx] is None:
                p.children[cIdx] = TrieNode()
            p = p.children[cIdx]
        if p.val is None:
            self.size += 1
        p.val = val

    # delete key
    def remove(self, key):
        if not self.containsKey(key):
            return

        self.root = self.removeHelper(self.root, key, 0)
        self.size -= 1

    def removeHelper(self, node, key, idx):
        # I guess node would not be None
        if not node:
            return None

        if idx == len(key):
            # No return here
            node.val = None
        else:
            # postorder traverse
            c = key[idx]
            node.children[ord(c) - ord("a")] = self.removeHelper(node.children[ord(c) - ord("a")], key, idx + 1)

        # decide if node need be deleted
        if node.val or node == self.root:
            return node

        for c in range(R):
            if node.children[c]:
                return node

        return None

    # Read
    def getNode(self, node, key):
        p = node
        for i in range(len(key)):
            if not p:
                return None
            c = key[i]
            p = p.children[ord(c) - ord("a")]

        return p

    def get(self, key):
        x = self.getNode(self.root, key) 
        if x is None:
            return None

        return x.val

    def containsKey(self, key):
        return self.get(key) is not None

    def hasKeyWithPrefix(self, prefix):
        return self.getNode(self.root, prefix) is not None

    def shortestPrefixOf(self, query):
        p = self.root
        for i in range(len(query)):
            if not p:
                return ""

            if p.val:
                return query[:i]

            c = query[i]
            p = p.children[ord(c) - ord("a")]

        if p and p.val:
            return query

        return ""

    def longestPrefixOf(self, query):
        p = self.root
        maxLen = 0

        for i in range(len(query)):
            if not p:
                break

            if p.val:
                maxLen = i

            c = query[i]
            p = p.children[ord(c) - ord("a")]

        if p and p.val:
            return query

        return query[:maxLen]


    def keyWithPrefix(self, prefix):
        res = []

        node = self.getNode(self.root, prefix)
        if not node:
            return res

        self.kwpTraverse(node, list(prefix), res)
        return res

    def kwpTraverse(self, node, path, res):
        if not node:
            return

        if node.val:
            res.append("".join(path))

        for c in range(R):
            path.append(chr(c + ord("a")))
            self.kwpTraverse(node.children[c], path, res)
            path.pop()


    def keyWithPattern(self, pattern):
        res = []
        self.kwPaTraverse(self.root, [], pattern, 0, res)
        return res

    def kwPaTraverse(self, node, path, pattern, idx, res):
        if not node:
            return

        if idx == len(pattern):
            if node.val:
                res.append("".join(path))
            return

        c = pattern[idx]
        if c == ".":
            for d in range(R):
                path.append(chr(d + ord("a")))
                self.kwPaTraverse(nod.children[d], path, pattern, idx + 1, res)
                path.pop()

        else:
            path.append(c)
            self.kwPaTraverse(nod.children[ord(c) - ord("a")], path, pattern, idx + 1, res)
            path.pop()

    def hasKeyWithPattern(self, pattern):
        return self.hkwpTraverse(self.root, pattern, 0)

    def hkwpTraverse(self, node, pattern, idx):
        if not node:
            return False

        if idx == len(pattern):
            return node.val is not None

        c = pattern[idx]

        if c == ".":
            for d in range(R):
                if self.hkwpTraverse(node.children[d], pattern, idx + 1):
                    return True

            return False

        else:
            return self.hkwpTraverse(node.children[ord(c) - ord("a")], pattern, idx + 1)


    def getSize(self):
        return self.size


class MapSum:

    def __init__(self):
        self.treeMap = TrieMap()


    def insert(self, key: str, val: int) -> None:
        self.treeMap.put(key, val)



    def sum(self, prefix: str) -> int:
        res = 0
        for key in self.treeMap.keyWithPrefix(prefix):
            res += self.treeMap.get(key)

        return res



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)