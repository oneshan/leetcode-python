# 3213 - Count Subarrays Where Max Element Appears at Least K Times
# Date: 2024-03-29
# Runtime: 869 ms, Memory: 30.9 MB
# Submission Id: 1216934073


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        left = count = ans = 0
        for right, num in enumerate(nums):
            if num == max_num:
                count += 1
            while count == k:
                if nums[left] == max_num:
                    count -= 1
                left += 1
            ans += left
        return ans