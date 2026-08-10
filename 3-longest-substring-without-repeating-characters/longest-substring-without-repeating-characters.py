class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        cha = set()
        for i in range(len(s)):
            while s[i] in cha:
                cha.remove(s[left])
                left += 1
            cha.add(s[i])
            max_len = max(max_len,i-left+1)
        return max_len