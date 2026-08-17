class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        dic = {}
        for i in range(m):
            if t[i] not in dic:
                dic[t[i]] = 1
            else:
                dic[t[i]] += 1 
        left = 0
        right = 0
        cnt = 0
        minlen = float("inf")
        sindex = -1
        while right< n:
            if s[right] in dic:
                if dic[s[right]] > 0:
                    cnt += 1
                dic[s[right]] -= 1
            while (cnt == m):
                if (right-left+1) < minlen:
                    minlen = right-left+1
                    sindex = left
                if s[left] in dic:
                    dic[s[left]] += 1
                    if dic[s[left]] > 0:
                        cnt -= 1
                left += 1
            right = right+1
        if sindex == -1:
            return ""
        return s[sindex:sindex+minlen]

                  
