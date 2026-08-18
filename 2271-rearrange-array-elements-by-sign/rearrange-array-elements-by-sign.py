class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for k in range(len(nums)):
            if nums[k]>0:
                pos.append(nums[k])
            else:
                neg.append(nums[k])
        nums = []
        for k in range(len(pos)):
            nums.append(pos[k])
            nums.append(neg[k])
        return nums