# 3436 - Find Subarray With Bitwise OR Closest to K
# Date: 2024-06-05
# Runtime: 4079 ms, Memory: 31.1 MB
# Submission Id: 1278450618


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        left = 0
        count = [0] * 30

        def update(num, val):
            for i in range(30):
                if num & (1 << i):
                    count[i] += val
        
        def calc(size):
            res = 0
            for i in range(30):
                if count[i] == size:
                    res |= (1 << i)
            return res

        for right, num in enumerate(nums):
            update(num, 1)
            ans = min(ans, abs(k - calc(right-left+1)))
            while left < right and calc(right-left+1) < k:
                update(nums[left], -1)
                left += 1
                ans = min(ans, abs(k - calc(right-left+1)))
                
        return ans