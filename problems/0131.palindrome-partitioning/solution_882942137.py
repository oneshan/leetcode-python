# 0131 - Palindrome Partitioning
# Date: 2023-01-22
# Runtime: 826 ms, Memory: 30.1 MB
# Submission Id: 882942137


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
        
        def backtrack(path, idx):
            if idx == n:
                ans.append(path[:])
                return
            for i in range(idx, n):
                if is_palindrome(idx, i):
                    path.append(s[idx:i+1])
                    backtrack(path, i+1)
                    path.pop()
            
            
        backtrack([], 0)
        return ans