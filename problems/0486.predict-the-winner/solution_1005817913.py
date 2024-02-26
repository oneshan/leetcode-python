# 0486 - Predict the Winner
# Date: 2023-07-28
# Runtime: 44 ms, Memory: 16.5 MB
# Submission Id: 1005817913


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def recur(i, j):
            if i == j:
                return nums[i]
            return max(nums[j] - recur(i, j-1),
                       nums[i] - recur(i+1, j))
        
        return recur(0, len(nums)-1) >= 0