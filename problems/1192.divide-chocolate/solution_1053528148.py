# 1192 - Divide Chocolate
# Date: 2023-09-19
# Runtime: 209 ms, Memory: 17.7 MB
# Submission Id: 1053528148


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        def check(max_sweet):
            curr_sum = group = 0
            for sweet in sweetness:
                curr_sum += sweet
                if curr_sum > max_sweet:
                    curr_sum = 0
                    group += 1
            # If we could not cut into k+1 pieces with max_sweet,
            # we should try a lower sweetness to divide it by
            return group <= k
        
        left, right = min(sweetness), sum(sweetness)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left