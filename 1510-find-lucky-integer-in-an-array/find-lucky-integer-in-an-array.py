class Solution:
    def findLucky(self, arr: list[int]) -> int:
        dic = {}
        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        s = -1
        for i,j in dic.items():
            if i == j and s<i :
                s = i
        return s
        