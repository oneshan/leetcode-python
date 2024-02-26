# 0249 - Group Shifted Strings
# Date: 2022-07-17
# Runtime: 59 ms, Memory: 14 MB
# Submission Id: 749241621


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        table = {}
        for string in strings:
            pattern = []
            first = string[0]
            pattern = tuple([(ord(ch) - ord(first)) % 26 for ch in string])        
            table.setdefault(pattern, [])
            table[pattern].append(string)
        return table.values()