# 1034 - Subarrays with K Different Integers
# Date: 2024-03-30
# Runtime: 331 ms, Memory: 19.2 MB
# Submission Id: 1217785907


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarrayAtMostK(nums, k) - self.subarrayAtMostK(nums, k-1)

    def subarrayAtMostK(self, nums, k):
        counter = defaultdict(int)
        ans = left = 0
        for right, num in enumerate(nums):
            counter[num] += 1
            while len(counter) > k:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    counter.pop(nums[left])
                left += 1
            ans += right - left + 1
        return ans