# 2738 - Count the Number of K-Free Subsets
# Date: 2024-04-03
# Runtime: 60 ms, Memory: 16.7 MB
# Submission Id: 1222488969


class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        table = defaultdict(list)
        for num in sorted(nums):
            table[num % k].append(num)
        
        ans = 1
        for arr in table.values():
            dp0, dp1 = 1, 2
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] == k:
                    dp0, dp1 = dp1, dp0 + dp1
                else:
                    dp0, dp1 = dp1, dp1 * 2
            ans *= dp1
        return ans