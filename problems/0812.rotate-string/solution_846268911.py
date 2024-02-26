# 0812 - Rotate String
# Date: 2022-11-19
# Runtime: 48 ms, Memory: 13.9 MB
# Submission Id: 846268911


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        len_s, len_goal = len(s), len(goal)
        if len_s != len_goal:
            return False
        if len_s == 0:
            return True
        
        prefix = [0] * len_goal
        j = 0
        for i in range(1, len_goal):
            while j and goal[i] != goal[j]:
                j = prefix[j-1]
            if goal[i] == goal[j]:
                prefix[i] = j + 1
                j += 1
        
        j = 0
        for i in range(len_s*2):
            si = i % len_s
            while j and s[si] != goal[j]:
                j = prefix[j-1]
            if s[si] == goal[j]:
                j += 1
            if j == len_goal:
                return True
        return False