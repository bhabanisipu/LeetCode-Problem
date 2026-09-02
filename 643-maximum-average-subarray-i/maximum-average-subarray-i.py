class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0
        sum = 0
        maxi = float('-inf')
        while right<len(nums):
            sum += nums[right]
            if right-left+1 == k:
                avg = sum / k
                maxi = max(maxi,avg)

                sum -= nums[left]
                left = left+1
            right+= 1
        return maxi