class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        seen = set()
        result = set()
        left = 0
        right = 0
        while right<n:
            if right-left+1 == 10:
                substring = s[left:right+1]
                if substring in seen:
                    result.add(substring)
                else:
                    seen.add(substring)
                left = left+1
            else:
                right= right+1
        return list(result)