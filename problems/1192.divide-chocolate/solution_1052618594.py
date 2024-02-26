# 1192 - Divide Chocolate
# Date: 2023-09-18
# Runtime: 192 ms, Memory: 17.9 MB
# Submission Id: 1052618594


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        def check(max_sweet):
            curr_sum = group = 0
            for sweet in sweetness:
                if curr_sum + sweet < max_sweet:
                    curr_sum += sweet
                else:
                    curr_sum = 0
                    group += 1
            return group >= k + 1
        
        left, right = min(sweetness), sum(sweetness) // (k+1)
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left