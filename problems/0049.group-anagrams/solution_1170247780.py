# 0049 - Group Anagrams
# Date: 2024-02-09
# Runtime: 91 ms, Memory: 20.4 MB
# Submission Id: 1170247780


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prime = [
            2,3,5,7,11,13,17,19,23,29,
            31,37,41,43,47,53,59,61,67,71,
            73,79,83,89,97,101,
        ]

        table = defaultdict(list)
        for s in strs:
            num = 1
            for ch in s:
                num *= prime[ord(ch) - ord('a')]
            table[num].append(s)
        
        return table.values()