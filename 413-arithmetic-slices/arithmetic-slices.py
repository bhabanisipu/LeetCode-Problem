class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        diff = nums[1] - nums[0]
        count = 0
        ans = 0
        for i in range(2,len(nums)):
            new_diff = nums[i]-nums[i-1]
            if new_diff == diff:
                count += 1
                ans += count
            else:
                count = 0
            diff = new_diff
        return ans