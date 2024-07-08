# 2071 - Longest Common Subsequence Between Sorted Arrays
# Date: 2024-06-02
# Runtime: 227 ms, Memory: 17 MB
# Submission Id: 1275432043


class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        n = len(arrays)

        counter = Counter()
        for array in arrays:
            counter += Counter(array)
        
        return [num for num in counter if counter[num] == n]