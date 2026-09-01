class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = float('inf')
        left = 0
        right = 0
        sum = 0
        while right<len(nums):
            sum += nums[right]
            while sum>= target:
                mini = min(right-left+1,mini)
                sum -= nums[left]
                left = left+1
            right = right+1
        if mini == float('inf'):
            return 0
        return mini