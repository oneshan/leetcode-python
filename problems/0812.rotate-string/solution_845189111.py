# 0812 - Rotate String
# Date: 2022-11-17
# Runtime: 49 ms, Memory: 13.8 MB
# Submission Id: 845189111


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        n = len(s)
        for i in range(n):
            for j in range(n):
                if s[(i+j) % n] != goal[j]:
                    break
            else:
                return True
        return False