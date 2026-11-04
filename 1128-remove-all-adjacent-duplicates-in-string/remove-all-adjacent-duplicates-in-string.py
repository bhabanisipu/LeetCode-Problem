class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = []
        l.append(s[0])
        i = 1
        while i<len(s):
            if l and s[i] == l[-1]:
                l.pop()
                i = i+1
            else:
                l.append(s[i])
                i = i+1
        return "".join(l)
