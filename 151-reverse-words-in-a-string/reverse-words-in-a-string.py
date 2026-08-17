class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        m = len(l)
        left = 0
        right = m-1
        while left <= right:
            l[left],l[right] = l[right],l[left]
            left += 1
            right -= 1
        return " ".join(l)