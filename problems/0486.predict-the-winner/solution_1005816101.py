# 0486 - Predict the Winner
# Date: 2023-07-28
# Runtime: 1599 ms, Memory: 745.5 MB
# Submission Id: 1005816101


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def recur(i, j, is_player1, score1, score2):
            if i > j:
                return score1 >= score2            
            if is_player1:
                left = recur(i+1, j, False, score1 + nums[i], score2)
                right = recur(i, j-1, False, score1 + nums[j], score2)
                return left or right
            left = recur(i+1, j, True, score1, score2 + nums[i])
            right = recur(i, j-1, True, score1, score2 + nums[j])
            return left and right
        
        return recur(0, len(nums)-1, True, 0, 0)