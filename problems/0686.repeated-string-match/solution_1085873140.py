# 0686 - Repeated String Match
# Date: 2023-10-28
# Runtime: 62 ms, Memory: 16.6 MB
# Submission Id: 1085873140


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a, len_b = len(a), len(b)
        
        # compute prefix
        prefix = [0] * len_b
        j = 0
        for i in range(1, len_b):
            while j and b[i] != b[j]:
                j = prefix[j-1]
            if b[i] == b[j]:
                j += 1
            prefix[i] = j
            
        # find pattern
        j = 0
        for i in range((len_b // len_a + 2) * len_a):
            while j and a[i % len_a] != b[j]:
                j = prefix[j-1]
            if a[i % len_a] == b[j]:
                j += 1
            if j == len_b:
                return ceil((i+1) / len_a)
        return -1