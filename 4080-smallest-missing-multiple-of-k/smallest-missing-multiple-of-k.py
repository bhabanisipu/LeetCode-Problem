class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        x = 0
        for i in range(1,maxi+2):
            if k*i not in nums:
                x = k*i
                break
        return x