# 0889 - Buddy Strings
# Date: 2023-07-03
# Runtime: 54 ms, Memory: 16.5 MB
# Submission Id: 985040836


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        p1 = p2 = -1
        for idx, (ch_s, ch_g) in enumerate(zip(s, goal)):
            if ch_s != ch_g:
                if p1 == -1:
                    p1 = idx
                elif p2 == -1:
                    p2 = idx
                else:
                    return False

        if p1 == -1:
            return len(set(goal)) != len(goal)

        if p2 == -1:
            return False
        
        return s[p1] == goal[p2] and s[p2] == goal[p1]