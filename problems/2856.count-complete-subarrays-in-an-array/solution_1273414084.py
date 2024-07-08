# 2856 - Count Complete Subarrays in an Array
# Date: 2024-05-31
# Runtime: 88 ms, Memory: 16.7 MB
# Submission Id: 1273414084


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        counter = defaultdict(int)
        ans = left = 0

        for right, num in enumerate(nums):
            counter[num] += 1
            while len(counter) == k:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
            ans += left

        return ans