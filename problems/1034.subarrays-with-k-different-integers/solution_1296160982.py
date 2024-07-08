# 1034 - Subarrays with K Different Integers
# Date: 2024-06-22
# Runtime: 332 ms, Memory: 19.8 MB
# Submission Id: 1296160982


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        
        ans = left = mid = 0
        for right in range(len(nums)):
            counter[nums[right]] += 1

            while len(counter) > k:
                counter[nums[mid]] -= 1
                if counter[nums[mid]] == 0:
                    counter.pop(nums[mid])
                left = mid = mid + 1

            while counter[nums[mid]] > 1:
                counter[nums[mid]] -= 1
                mid += 1
            
            if len(counter) == k:
                ans += (mid - left + 1)

        return ans