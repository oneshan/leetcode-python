# 0049 - Group Anagrams
# Date: 2023-08-23
# Runtime: 93 ms, Memory: 20.1 MB
# Submission Id: 1029600703


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[''.join(sorted(s))].append(s)
        return groups.values()