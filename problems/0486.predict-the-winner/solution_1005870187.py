# 0486 - Predict the Winner
# Date: 2023-07-28
# Runtime: 33 ms, Memory: 16.7 MB
# Submission Id: 1005870187


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        @cache
        def recur(left, right, is_player1):
            if left > right:
                return 0
            if is_player1:
                return max(recur(left+1, right, False) + nums[left],
                           recur(left, right-1, False) + nums[right])
            else:
                return min(recur(left+1, right, True) - nums[left],
                           recur(left, right-1, True) - nums[right])
        
        return recur(0, len(nums)-1, True) >= 0