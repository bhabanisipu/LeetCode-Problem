class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        r = len(s)
        x = len(t)
        i = 0
        j = 0
        while i<r:
            flag = False
            while j<x:
                if s[i] != t[j]:
                    j = j+1
                else:
                    i = i+1
                    j = j+1
                    flag = True
                    break
            if flag == False:
                return False
        return True
