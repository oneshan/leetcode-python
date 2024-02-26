# 2053 - Check if All Characters Have Equal Number of Occurrences
# Date: 2022-09-27
# Runtime: 62 ms, Memory: 14 MB
# Submission Id: 809774741


from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        table = defaultdict(int)
        for ch in s:
            table[ch] += 1
        
        return len(set(table.values())) == 1