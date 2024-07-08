# 1370 - Count Number of Nice Subarrays
# Date: 2024-05-31
# Runtime: 566 ms, Memory: 23.5 MB
# Submission Id: 1273383154


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = ans = count = 0
        odds = 0
        for right, num in enumerate(nums):
            if num & 1:
                odds += 1
                count = 0
            while left <= right and odds >= k:
                if odds == k:
                    count += 1
                odds -= nums[left] & 1
                left += 1
            ans += count

        return ans