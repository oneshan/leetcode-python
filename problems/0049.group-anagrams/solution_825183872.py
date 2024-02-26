# 0049 - Group Anagrams
# Date: 2022-10-18
# Runtime: 256 ms, Memory: 19.9 MB
# Submission Id: 825183872


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for ch in s:
                counter[ord(ch)-97] += 1
            table[tuple(counter)].append(s)
        return table.values()