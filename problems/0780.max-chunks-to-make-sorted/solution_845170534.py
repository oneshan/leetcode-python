# 0780 - Max Chunks To Make Sorted
# Date: 2022-11-17
# Runtime: 25 ms, Memory: 13.8 MB
# Submission Id: 845170534


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans, max_idx = 0, -1
        for idx, num in enumerate(arr):
            max_idx = max(max_idx, num)
            if idx == max_idx:
                ans += 1
        return ans