class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = {}
        max_len = 0
        n = len(fruits)
        left = 0
        for right in range(n):
            if fruits[right] in dic:
                dic[fruits[right]] += 1
            else:
                dic[fruits[right]] = 1
            while len(dic) >2:
                dic[fruits[left]] -= 1
                if dic[fruits[left]] == 0:
                    del dic[fruits[left]]
                left += 1
            max_len = max(max_len,right-left+1)
        return max_len