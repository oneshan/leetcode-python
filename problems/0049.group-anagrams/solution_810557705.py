# 0049 - Group Anagrams
# Date: 2022-09-28
# Runtime: 237 ms, Memory: 18.5 MB
# Submission Id: 810557705


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for s in strs:
            table[tuple(sorted(s))].append(s)
        return table.values()