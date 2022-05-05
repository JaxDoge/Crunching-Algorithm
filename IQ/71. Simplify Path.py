71. Simplify Path


# stack
# if name is . or empty string, ignore it
# if name is .. and stack is empty, ignore it
class Solution:
    def simplifyPath(self, path: str) -> str:
        dirNames = path.split("/")
        stack = []

        for name in dirNames:
            if name == '..':
                if len(stack) > 0:
                    stack.pop()
            elif name and name != '.':
                stack.append(name)

        return "/" + "/".join(stack)