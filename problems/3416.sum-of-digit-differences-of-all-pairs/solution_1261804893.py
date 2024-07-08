# 3416 - Sum of Digit Differences of All Pairs
# Date: 2024-05-19
# Runtime: 937 ms, Memory: 27.8 MB
# Submission Id: 1261804893


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0
        while nums[0]:
            counter = [0] * 10
            for i in range(n):
                nums[i], digit = divmod(nums[i], 10)
                counter[digit] += 1
            
            count = n
            for i in range(10):
                count -= counter[i]
                ans += counter[i] * count
        return ans