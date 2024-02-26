# 0049 - Group Anagrams
# Date: 2023-08-23
# Runtime: 97 ms, Memory: 20.6 MB
# Submission Id: 1029602479


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for s in strs:
            table[tuple(sorted(s))].append(s)
        return table.values()