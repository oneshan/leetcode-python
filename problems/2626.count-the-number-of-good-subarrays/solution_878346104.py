# 2626 - Count the Number of Good Subarrays
# Date: 2023-01-15
# Runtime: 750 ms, Memory: 31.8 MB
# Submission Id: 878346104


from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left, n = 0, len(nums)
        table = defaultdict(int)
        ans = curr_pair = 0
        for right, num in enumerate(nums):
            curr_pair += table[num]
            table[num] += 1
            while curr_pair >= k:
                ans += n-right
                curr_pair -= (table[nums[left]]-1)
                table[nums[left]] -= 1
                left += 1
        
        return ans
            