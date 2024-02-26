# 0049 - Group Anagrams
# Date: 2022-09-28
# Runtime: 108 ms, Memory: 19.9 MB
# Submission Id: 810555729


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch)-ord('a')] += 1
            table[tuple(key)].append(s)
        return table.values()