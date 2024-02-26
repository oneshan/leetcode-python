# 2053 - Check if All Characters Have Equal Number of Occurrences
# Date: 2022-09-27
# Runtime: 67 ms, Memory: 13.8 MB
# Submission Id: 809778716


from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        table = Counter(s)
        max_freq = len(s) // len(table)
        return all(freq == max_freq for freq in table.values())