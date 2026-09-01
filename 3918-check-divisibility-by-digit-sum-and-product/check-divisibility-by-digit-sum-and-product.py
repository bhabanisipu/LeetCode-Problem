class Solution:
    def checkDivisibility(self, n: int) -> bool:
        r = str(n)
        s = 0
        p = 1
        for i in r:
            s += int(i)
            p *= int(i)
        
        k = s+p
        if n%k == 0:
            return True
        return False