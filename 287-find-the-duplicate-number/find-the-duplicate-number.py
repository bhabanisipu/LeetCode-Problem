class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        r = 0
        for i in range(len(nums)):
            if nums[i] in s:
                r = nums[i]
                break
            else:
                s.add(nums[i])
        return r