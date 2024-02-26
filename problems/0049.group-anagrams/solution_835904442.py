# 0049 - Group Anagrams
# Date: 2022-11-03
# Runtime: 250 ms, Memory: 17.9 MB
# Submission Id: 835904442


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for s in strs:
            mask = ''.join(sorted(s))
            table[mask].append(s)
        return table.values()