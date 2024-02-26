# 0049 - Group Anagrams
# Date: 2023-08-23
# Runtime: 97 ms, Memory: 20.4 MB
# Submission Id: 1029602079


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        mapping = dict(zip('abcdefghijklmnopqrstuvwxyz', prime))
        
        table = defaultdict(list)
        for s in strs:
            pattern = 1
            for ch in s:
                pattern *= mapping[ch]
            table[pattern].append(s)
        return table.values()