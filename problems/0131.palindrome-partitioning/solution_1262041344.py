# 0131 - Palindrome Partitioning
# Date: 2024-05-19
# Runtime: 484 ms, Memory: 35.4 MB
# Submission Id: 1262041344


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(arr, i):
            if i == n:
                ans.append(arr[:])
                return
            for j in range(i, n):
                if is_palindrome(i, j):
                    arr.append(s[i:j+1])
                    backtrack(arr, j+1)
                    arr.pop()

        backtrack([], 0)
        return ans