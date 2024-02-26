# 1573 - Find Two Non-overlapping Sub-arrays Each With Target Sum
# Date: 2022-11-19
# Runtime: 3155 ms, Memory: 35.7 MB
# Submission Id: 846311308


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        ans = min_left = float('inf')
        
        prefix = {0: -1}
        curr_sum = 0
        for idx, num in enumerate(arr):
            curr_sum += num
            prefix[curr_sum] = idx
            
        curr_sum = 0
        for idx, num in enumerate(arr):
            curr_sum += num
            if curr_sum - target in prefix:
                min_left = min(min_left, idx - prefix[curr_sum-target])
            if curr_sum + target in prefix:
                ans = min(ans, min_left + (prefix[curr_sum+target] - idx))
                
        return ans if ans != float('inf') else -1