class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1
        sum = 0
        l = []
        while left<right:
            sum = numbers[left]+numbers[right]
            if sum == target:
                return [left+1,right+1]
                break
            elif sum>target:
                right = right-1
            else:
                left = left+1
        return l