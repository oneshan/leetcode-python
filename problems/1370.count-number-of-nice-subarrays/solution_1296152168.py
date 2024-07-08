# 1370 - Count Number of Nice Subarrays
# Date: 2024-06-22
# Runtime: 565 ms, Memory: 23.4 MB
# Submission Id: 1296152168


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = left = cnt = 0
        for right in range(len(nums)):
            if nums[right] & 1:
                k -= 1
                cnt = 0
            while k == 0:
                k += nums[left] & 1
                left += 1
                cnt += 1
            ans += cnt
        return ans