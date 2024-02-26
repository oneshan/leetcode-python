# 3141 - Minimum Size Subarray in Infinite Array
# Date: 2023-10-01
# Runtime: 330 ms, Memory: 25.4 MB
# Submission Id: 1063652473


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        r, c = divmod(target, total)
        ans = 0
        if r:
            ans = (r-1) * n
            target = c + total
        
        left = curr_sum = 0
        length = float('inf')
        for right in range(n*3):
            curr_sum += nums[right % n]
            while curr_sum > target and left < n:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                length = min(length, right - left + 1)
            if left == n:
                break
        return (ans + length) if length != float('inf') else -1