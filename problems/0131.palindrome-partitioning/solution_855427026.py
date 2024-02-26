# 0131 - Palindrome Partitioning
# Date: 2022-12-06
# Runtime: 1861 ms, Memory: 30.1 MB
# Submission Id: 855427026


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
        
        def backtracking(path, start):
            if start == n:
                ans.append(path[:])
                return
            for i in range(start, n):
                if is_palindrome(start, i):
                    path.append(s[start:i+1])
                    backtracking(path, i+1)
                    path.pop()
        
        backtracking([], 0)
        return ans