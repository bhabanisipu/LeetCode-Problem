class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxi = 0
        smax = 0
        for i in nums:
            if i > maxi:
                smax = maxi
                maxi = i
            elif i>smax:
                smax = i
        return (maxi-1)*(smax-1)