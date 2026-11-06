class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1]*n

        prefix_prod = 1
        prefix_pr = [1]*n
        for i in range(n):
            prefix_pr[i] = prefix_prod
            prefix_prod *= nums[i]

        suffix_prod = 1
        suffix_pr = [1]*n
        for i in range(n-1,-1,-1):
            suffix_pr[i] = suffix_prod
            suffix_prod *= nums[i]

        for i in range(n):
            answer[i] = prefix_pr[i]*suffix_pr[i]
        return answer 