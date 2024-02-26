# 0392 - Is Subsequence
# Date: 2022-07-11
# Runtime: 37 ms, Memory: 14.5 MB
# Submission Id: 744106750


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        letters = {}
        for idx, ch in enumerate(t):
            letters.setdefault(ch, [])
            letters[ch].append(idx)
        
        idx = -1
        for ch in s:
            if ch not in letters:
                return False
            match_idx = bisect.bisect_right(letters[ch], idx)
            if match_idx == len(letters[ch]):
                return False
            idx = letters[ch][match_idx]
        return True