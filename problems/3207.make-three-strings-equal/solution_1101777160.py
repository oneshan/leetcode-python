# 3207 - Make Three Strings Equal
# Date: 2023-11-19
# Runtime: 38 ms, Memory: 16.3 MB
# Submission Id: 1101777160


class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        total = len(s1) + len(s2) + len(s3)
        min_len = min(len(s1), len(s2), len(s3))
        for i in range(min_len):
            if not (s1[i] == s2[i] == s3[i]):
                min_len = i
                break
        
        if min_len == 0:
            return -1
        return total - min_len * 3