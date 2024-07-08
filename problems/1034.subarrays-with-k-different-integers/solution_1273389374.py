# 1034 - Subarrays with K Different Integers
# Date: 2024-05-31
# Runtime: 391 ms, Memory: 19.9 MB
# Submission Id: 1273389374


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def at_most(goal):
            counter = defaultdict(int)
            res = left = 0
            for right, num in enumerate(nums):
                counter[num] += 1
                while left <= right and len(counter) > goal:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        del counter[nums[left]]
                    left += 1
                res += right - left + 1
            return res

        return at_most(k) - at_most(k-1)