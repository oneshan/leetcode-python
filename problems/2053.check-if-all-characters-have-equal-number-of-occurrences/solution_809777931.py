# 2053 - Check if All Characters Have Equal Number of Occurrences
# Date: 2022-09-27
# Runtime: 84 ms, Memory: 13.9 MB
# Submission Id: 809777931


from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        table = defaultdict(int)
        for ch in s:
            table[ch] += 1
        
        max_freq = len(s) // len(table)
        return all(freq == max_freq for freq in table.values())