# 0345 - Reverse Vowels of a String
# Date: 2022-10-13
# Runtime: 57 ms, Memory: 15 MB
# Submission Id: 821631241


class Solution:
    def reverseVowels(self, s: str) -> str:
        s_lst = list(s)
        left, right = 0, len(s)-1
        while left < right:
            while left < right and s[left] not in 'AEIOUaeiou':
                left += 1
            while left < right and s[right] not in 'AEIOUaeiou':
                right -= 1
            s_lst[left], s_lst[right] = s_lst[right], s_lst[left]
            left += 1
            right -= 1
        return ''.join(s_lst)