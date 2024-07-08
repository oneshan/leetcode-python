# 3307 - Find the Maximum Sum of Node Values
# Date: 2024-05-19
# Runtime: 954 ms, Memory: 28 MB
# Submission Id: 1261981969


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)

        sum_o, sum_e = float('-inf'), 0
        for num in nums:
            odd, even = num ^ k, num
            sum_o, sum_e = max(sum_o + even, sum_e + odd), max(sum_o + odd, sum_e + even)
        
        return sum_e