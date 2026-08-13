class Solution:
    def subarraysWithKDistinct(self, num: List[int], go: int) -> int:
        def fun(nums,k):
            n = len(nums)
            left = 0
            cnt = 0
            freq = {}
            for right in range(len(nums)):
                if nums[right] not in freq or freq[nums[right]] == 0:
                    k -=1
                freq[nums[right]] = freq.get(nums[right],0) + 1
                while k<0:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        k = k+1
                    left += 1
                cnt += right-left +1
            return cnt
        return fun(num,go) - fun(num,go-1)

                
