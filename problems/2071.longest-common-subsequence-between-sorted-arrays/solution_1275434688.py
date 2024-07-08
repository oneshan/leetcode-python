# 2071 - Longest Common Subsequence Between Sorted Arrays
# Date: 2024-06-02
# Runtime: 185 ms, Memory: 17 MB
# Submission Id: 1275434688


class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        n = len(arrays)

        ans = set(arrays[0])
        for i in range(1, n):
            ans = ans & set(arrays[i])
        return sorted(ans)