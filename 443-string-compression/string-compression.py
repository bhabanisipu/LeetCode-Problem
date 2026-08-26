class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        i = 0
        while i < len(chars):
            count = 1
            j = i + 1
            while j < len(chars) and chars[i] == chars[j]:
                count += 1
                j += 1

            s += chars[i]
            if count > 1:
                s += str(count)
            i = j
        for k in range(len(s)):
            chars[k] = s[k]
        return len(s)