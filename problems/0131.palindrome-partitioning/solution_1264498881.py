# 0131 - Palindrome Partitioning
# Date: 2024-05-22
# Runtime: 458 ms, Memory: 35.3 MB
# Submission Id: 1264498881


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []

        @cache
        def is_palindrome(left, right):
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return is_palindrome(left+1, right-1)

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