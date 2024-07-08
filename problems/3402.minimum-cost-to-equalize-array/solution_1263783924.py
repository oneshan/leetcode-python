# 3402 - Minimum Cost to Equalize Array
# Date: 2024-05-21
# Runtime: 6255 ms, Memory: 31.7 MB
# Submission Id: 1263783924


class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        n = len(nums)
        MOD = 1_000_000_007

        max_num = max(nums)
        max_diff = max(nums) - min(nums)
        count = sum(max_num - num for num in nums)

        if n <= 2 or cost1 * 2 <= cost2:
            return cost1 * count % MOD

        def cost(diff, count):
            if count - diff >= diff:
                op2 = count >> 1
                op1 = count & 1
            else:
                op2 = count - diff
                op1 = count - (count - diff) * 2
            return op2 * cost2 + op1 * cost1

        ans = float('inf')
        for d in range(max_diff, max_diff * 2 + 1):
            ans = min(ans, cost(d, count))
            count += n
            
        return ans % MOD