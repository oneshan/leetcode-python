# 2053 - Check if All Characters Have Equal Number of Occurrences
# Date: 2022-09-27
# Runtime: 75 ms, Memory: 14 MB
# Submission Id: 809777534


from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        table = defaultdict(int)
        for ch in s:
            table[ch] += 1
        
        max_freq = len(s) // len(table)
        for freq in table.values():
            if freq != max_freq:
                return False
        return True