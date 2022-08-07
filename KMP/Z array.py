# Z Algorithm

# Z Algorithm is similar to KMP. It will generate a z-array that indicate the length of prefixed substring start from each index
# z[0] is always the length of the original string


def getZArr(string):
    n = len(string)
    zArr = [0] * n
    zArr[0] = n
    l = r = 0

    for i in range(1, n):
        if i > R:
            l = r = i
            while r < n and string[r - l] == string[r]:
                r += 1

            zArr[i] = r - l
            r -= 1

        else:
            k = i - l

            if zArr[k] < r - l + 1:
                zArr[i] = zArr[k]

            else:
                l = i
                while r < n and string[r - l] == string[r]:
                    r += 1

                zArr[i] = r - l
                r -= 1
    return zArr

# find the pattern

def search(text, pattern):
    concat = pattern + "$" + text
    zArr = getZArr(concat)

    for zv in zArr:
        if zv == len(pattern):
            print(zv - 1 - len(pattern))