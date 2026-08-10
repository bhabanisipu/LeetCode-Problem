class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        leftsum = 0
        maxi = 0
        for i in range(k):
            leftsum = leftsum + cardPoints[i]
        maxi = max(maxi,leftsum)
        righ = n-1
        rightsum = 0
        for i in range(k-1,-1,-1):
            leftsum -= cardPoints[i]
            leftsum += cardPoints[righ]
            righ = righ-1
            maxi = max(maxi,leftsum)
        return maxi
       