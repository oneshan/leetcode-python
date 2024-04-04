# 2868 - Continuous Subarrays
# Date: 2024-03-26
# Runtime: 713 ms, Memory: 26.9 MB
# Submission Id: 1214117990


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        counter = defaultdict(int)

        ans = left = 0
        for right, num in enumerate(nums):
            counter[num] += 1
            while max(counter) - min(counter) > 2:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    counter.pop(nums[left])
                left += 1    
            ans += (right - left + 1)

        return ans