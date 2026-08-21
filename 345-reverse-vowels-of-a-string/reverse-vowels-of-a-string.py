class Solution:
    def reverseVowels(self, s: str) -> str:

        l = list(s)
        n = len(l)

        vowels = ['A','E','I','O','U','a','e','i','o','u']

        left = 0
        right = n - 1

        while left <= right:

            if l[left] not in vowels:
                left += 1

            elif l[right] not in vowels:
                right -= 1

            else:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1

        return ''.join(l)