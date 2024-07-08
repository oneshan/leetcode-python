# 2071 - Longest Common Subsequence Between Sorted Arrays
# Date: 2024-06-02
# Runtime: 197 ms, Memory: 17 MB
# Submission Id: 1275437267


class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        n = len(arrays)

        def get_lcs(arr1, arr2):
            res = []
            idx1 = idx2 = 0
            while idx1 < len(arr1) and idx2 < len(arr2):
                if arr1[idx1] == arr2[idx2]:
                    res.append(arr1[idx1])
                    idx1 += 1
                    idx2 += 1
                elif arr1[idx1] < arr2[idx2]:
                    idx1 += 1
                else:
                    idx2 += 1
            return res

        ans = arrays[0]
        for i in range(1, n):
            if not ans:
                return []
            ans = get_lcs(ans, arrays[i])
        return ans