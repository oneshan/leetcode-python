# 2624 - Difference Between Element Sum and Digit Sum of an Array
# Date: 2023-01-15
# Runtime: 139 ms, Memory: 14.2 MB
# Submission Id: 878331172


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        def get_digit_sum(num):
            total = 0
            while num:
                num, r = divmod(num, 10)
                total += r
            return total
        
        total_sum = digit_sum = 0
        for num in nums:
            total_sum += num
            digit_sum += get_digit_sum(num)
        return total_sum - digit_sum