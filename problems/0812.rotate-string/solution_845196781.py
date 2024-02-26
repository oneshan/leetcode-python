# 0812 - Rotate String
# Date: 2022-11-17
# Runtime: 59 ms, Memory: 13.8 MB
# Submission Id: 845196781


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal):
            return False
        if n == 0:
            return True
        
        shifts = [1] * (n+1)
        left = -1
        for right in range(n):
            while left >= 0 and goal[left] != goal[right]:
                left -= shifts[left]
            shifts[right+1] = right - left
            left += 1
            
        print(shifts)
        
        match_len = 0
        for ch in s+s:
            while match_len >= 0 and goal[match_len] != ch:
                match_len -= shifts[match_len]
            match_len += 1
            if match_len == n:
                return True
        return False