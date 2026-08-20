class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        maxarea = 0
        while left<=right:
            area = min(height[left],height[right])*(right-left)
            maxarea = max(maxarea,area)
            if height[left]<height[right]:
                left = left+1
            else:
                right = right-1
        return maxarea