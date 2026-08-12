class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def fun(nums,k):
            n = len(nums)
            cnt = 0
            if k<0:
                return 0
            left = 0
            sum = 0
            for right in range(n):
                sum += nums[right]
                while sum >k:
                    sum -= nums[left]
                    left += 1
                cnt = cnt+(right-left+1)
            return cnt
        return fun(nums,goal) - fun(nums,goal-1)
                