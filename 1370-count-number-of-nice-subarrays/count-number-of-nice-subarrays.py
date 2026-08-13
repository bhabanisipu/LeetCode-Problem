class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def fun(num,go):
            n = len(nums)
            left = 0
            sum = 0
            cnt = 0
            for right in range(n):
                sum += nums[right] % 2
                while sum > go:
                    sum -= nums[left] %2
                    left += 1
                cnt += right-left +1
            return cnt
        return fun(nums,k) - fun(nums,k-1)
        