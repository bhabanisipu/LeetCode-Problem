class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        left = 0
        dic = {'a':0,'b':0,'c':0}
        for right in range(n):
            dic[s[right]] += 1
            while dic['a']>0 and dic['b']>0 and dic['c']>0:
                cnt += len(s) - right
                dic[s[left]] -= 1
                left += 1
        return cnt
