# 0049 - Group Anagrams
# Date: 2022-07-17
# Runtime: 141 ms, Memory: 19.9 MB
# Submission Id: 748908431


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            pattern = [0] * 26
            for ch in s:
                pattern[ord(ch) - ord('a')] += 1
            pattern = tuple(pattern)
            ans.setdefault(pattern, [])
            ans[pattern].append(s)
        return ans.values()