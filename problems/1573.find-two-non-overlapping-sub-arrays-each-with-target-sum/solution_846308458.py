# 1573 - Find Two Non-overlapping Sub-arrays Each With Target Sum
# Date: 2022-11-19
# Runtime: 2247 ms, Memory: 27.7 MB
# Submission Id: 846308458


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        ans = float('inf')
        prev_min = [float('inf')] * len(arr)
        
        curr_sum = left = 0
        for right in range(len(arr)):
            curr_sum += arr[right]
            while left < right and curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                ans = min(ans, prev_min[left-1] + right-left+1)
                prev_min[right] = min(prev_min[right-1], right-left+1)
            else:
                prev_min[right] = prev_min[right-1]
        
        return ans if ans != float('inf') else -1
