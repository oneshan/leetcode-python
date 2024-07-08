# 1370 - Count Number of Nice Subarrays
# Date: 2024-06-22
# Runtime: 563 ms, Memory: 23.5 MB
# Submission Id: 1296157649


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        ans = 0
        left = mid = 0

        for right in range(len(nums)):
            if nums[right] & 1:
                k -= 1

            if k > 0:
                continue

            while k < 0:
                if nums[left] & 1:
                    k += 1
                left = mid = left + 1
            
            while nums[mid] & 1 == 0:
                mid += 1
            ans += (mid - left + 1)

        return ans