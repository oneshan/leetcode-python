# 2231 - Find First Palindromic String in the Array
# Date: 2024-02-13
# Runtime: 82 ms, Memory: 16.8 MB
# Submission Id: 1173850570


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        def is_palindrome(word):
            left, right = 0, len(word)-1
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True

        for word in words:
            if is_palindrome(word):
                return word
        return ''