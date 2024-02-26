# 2559 - Maximum Number of Non-overlapping Palindrome Substrings
# Date: 2022-11-13
# Runtime: 49 ms, Memory: 14.3 MB
# Submission Id: 842374035


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        intervals = []
        
        def palindrome(left, right):
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                if right - left + 1 >= k:
                    intervals.append([left, right+1])
                    break
                left -= 1
                right += 1
        
        palindrome(0, 0)
        for i in range(1, n):
            palindrome(i-1, i)
            palindrome(i, i)
            
        count = 0 
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i+1][0] < intervals[i][1]:
                count += 1
                intervals[i+1][1] = min(intervals[i+1][1], intervals[i][1])
        return len(intervals) - count