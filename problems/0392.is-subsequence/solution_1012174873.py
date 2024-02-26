# 0392 - Is Subsequence
# Date: 2023-08-04
# Runtime: 29 ms, Memory: 16.7 MB
# Submission Id: 1012174873


from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        table = defaultdict(list)
        for idx, ch in enumerate(t):
            table[ch].append(idx)
        
        curr_idx = -1
        for ch in s:
            if ch not in table:
                return False
            match_idx = bisect.bisect_right(table[ch], curr_idx)
            if match_idx == len(table[ch]):
                return False
            curr_idx = table[ch][match_idx]
        return True