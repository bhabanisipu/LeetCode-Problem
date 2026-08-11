class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        dic = {}
        max_len = 0
        left = 0
        max_freq = 0
        for i in range(n):
            if s[i] not in dic:
                dic[s[i]] =1
            else:
                dic[s[i]] += 1
            max_freq = max(max_freq, dic[s[i]])
            while (i-left+1) - max_freq > k:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                left += 1
            max_len = max(max_len,i-left+1)
        return max_len