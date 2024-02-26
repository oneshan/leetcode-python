# 0812 - Rotate String
# Date: 2022-11-17
# Runtime: 54 ms, Memory: 13.9 MB
# Submission Id: 845191374


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s+s