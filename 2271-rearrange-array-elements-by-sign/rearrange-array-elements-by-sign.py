class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for k in range(len(nums)):
            if nums[k]>0:
                pos.append(nums[k])
            else:
                neg.append(nums[k])
        num = []
        for k in range(len(pos)):
            num.append(pos[k])
            num.append(neg[k])
        return num