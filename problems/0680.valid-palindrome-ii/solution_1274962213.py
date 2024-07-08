# 0680 - Valid Palindrome II
# Date: 2024-06-02
# Runtime: 97 ms, Memory: 19 MB
# Submission Id: 1274962213


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_valid(left, right, has_delete):
            while left < right:
                if s[left] != s[right]:
                    if has_delete:
                        return False
                    return is_valid(left+1, right, True) or is_valid(left, right-1, True)
                left += 1
                right -= 1
            return True

        return is_valid(0, len(s)-1, False)