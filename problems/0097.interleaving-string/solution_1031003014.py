# 0097 - Interleaving String
# Date: 2023-08-25
# Runtime: 42 ms, Memory: 17.2 MB
# Submission Id: 1031003014


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if len3 != len1 + len2:
            return False
        
        seen = set()
        stack = [(0, 0, 0)]
        while stack:
            p1, p2, p3 = stack.pop()
            if (p1, p2, p3) in seen:
                continue
            seen.add((p1, p2, p3))
            if p1 == len1:
                if s2[p2:] == s3[p3:]:
                    return True
                continue
            if p2 == len2:
                if s1[p1:] == s3[p3:]:
                    return True
                continue
            if s1[p1] == s3[p3]:
                stack.append((p1+1, p2, p3+1))
            if s2[p2] == s3[p3]:
                stack.append((p1, p2+1, p3+1))
        return False