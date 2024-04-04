# 2738 - Count the Number of K-Free Subsets
# Date: 2024-04-03
# Runtime: 94 ms, Memory: 16.8 MB
# Submission Id: 1222485696


class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        table = defaultdict(list)
        for num in sorted(nums):
            table[num % k].append(num)
        
        dp0 = dp1 = 0
        for i in range(k):
            prev = 1000
            for num in table[i]:
                dp0, dp1 = dp0 + dp1, 1 + dp0 + (0 if num - prev == k else dp1)
                prev = num

        return dp0 + dp1 + 1