面试题 01.06. Compress String LCCI


# Simple immitation
class Solution:
    def compressString(self, S: str) -> str:
        if len(S) < 3:
            return S

        ans = []
        
        curC = S[0]
        cnt = 0

        for c in S:
            if curC == c:
                cnt += 1
                continue
            else:
                ans.append(curC)
                ans.append(str(cnt))
                curC = c
                cnt = 1
                
        ans.append(curC)
        ans.append(str(cnt))                

        ansS = "".join(ans)
        return ansS if len(ansS) < len(S) else S