# 2473 - Max Sum of a Pair With Equal Sum of Digits
# Date: 2022-09-28
# Runtime: 2248 ms, Memory: 29.4 MB
# Submission Id: 810571281


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_of_digit(val):
            _sum = 0
            while val:
                val, digit = divmod(val, 10)
                _sum += digit
            return _sum
        
        table = {}
        ans = -1
        for num in nums:
            key = sum_of_digit(num) 
            if key in table:
                ans = max(ans, table[key] + num)
            table[key] = max(table.get(key, -1), num)
        return ans