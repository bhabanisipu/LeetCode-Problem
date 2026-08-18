class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split(".")
        l2 = version2.split(".")

        maxi = max(len(l1),len(l2))
        for i in range(maxi):
            if i < len(l1):
                num1 = int(l1[i])
            else:
                num1 = 0
            if i < len(l2):
                nums2 = int(l2[i])
            else:
                nums2 = 0
            if num1<nums2:
                return -1
            elif num1>nums2:
                return 1
        return 0

