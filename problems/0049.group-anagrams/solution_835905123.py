# 0049 - Group Anagrams
# Date: 2022-11-03
# Runtime: 142 ms, Memory: 19.9 MB
# Submission Id: 835905123


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for s in strs:
            mask = [0] * 26
            for ch in s:
                mask[ord(ch)-ord('a')] += 1
            table[tuple(mask)].append(s)
        return table.values()