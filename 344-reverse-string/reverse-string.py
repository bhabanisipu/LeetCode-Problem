class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        left = 0
        right = n-1
        while left<=right:
            s[left],s[right] = s[right],s[left]
            left = left+1
            right = right-1
        
        