# 2473 - Max Sum of a Pair With Equal Sum of Digits
# Date: 2022-09-28
# Runtime: 2462 ms, Memory: 29.2 MB
# Submission Id: 810572396


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
            if key not in table:
                table[key] = num
            else:
                ans = max(ans, table[key] + num)
                table[key] = max(table[key], num)
        return ans