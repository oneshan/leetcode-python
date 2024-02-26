# 2059 - Unique Length-3 Palindromic Subsequences
# Date: 2023-11-14
# Runtime: 115 ms, Memory: 21.7 MB
# Submission Id: 1098406123


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        table = defaultdict(list)
        for idx, ch in enumerate(s):
            table[ch].append(idx)
            
        ans = 0
        for center in table:
            for corner in table:
                if center == corner:
                    if len(table[center]) >= 3:
                        ans += 1
                    continue
                left, right = table[corner][0], table[corner][-1]
                idx = bisect.bisect_left(table[center], left)
                if idx < 0 or idx > len(table[center]) - 1:
                    continue
                if left < table[center][idx] < right:
                    ans += 1
        return ans