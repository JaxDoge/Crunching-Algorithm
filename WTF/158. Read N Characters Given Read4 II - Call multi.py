158. Read N Characters Given Read4 II - Call multiple times



class Solution:
    def __init__(self):
        def reader():
            buf4=['']*4
            while n:=read4(buf4):
                yield from buf4[:n]
        self.it=reader()
        
    def read(self, buf: List[str], n: int) -> int:
        i=-1
        for i,c in zip(range(n),self.it):
            buf[i]=c
        return i+1