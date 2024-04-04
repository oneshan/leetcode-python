# 1034 - Subarrays with K Different Integers
# Date: 2024-03-30
# Runtime: 279 ms, Memory: 20 MB
# Submission Id: 1217789852


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        
        ans = left = curr_count = 0
        for right, num in enumerate(nums):
            counter[num] += 1
            if len(counter) < k:
                continue

            if len(counter) > k:
                curr_count = 0
                while len(counter) > k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        counter.pop(nums[left])
                    left += 1
            
            while counter[nums[left]] > 1:
                counter[nums[left]] -= 1
                left += 1
                curr_count += 1
            ans += curr_count + 1

        return ans