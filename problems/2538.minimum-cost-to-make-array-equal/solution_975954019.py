# 2538 - Minimum Cost to Make Array Equal
# Date: 2023-06-21
# Runtime: 910 ms, Memory: 31.8 MB
# Submission Id: 975954019


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        def get_cost(val):
            return sum(abs(val-num) * c for num, c in zip(nums, cost))
        
        left, right = min(nums), max(nums)
        if left == right:
            return get_cost(nums[0])
        
        while left < right:
            mid = (left + right) // 2
            cost1 = get_cost(mid)
            cost2 = get_cost(mid+1)
            ans = min(cost1, cost2)
            if cost1 > cost2:
                left = mid + 1
            else:
                right = mid
        return ans