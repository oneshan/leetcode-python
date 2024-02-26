# 1448 - Maximum 69 Number
# Date: 2023-09-17
# Runtime: 31 ms, Memory: 16.3 MB
# Submission Id: 1051641179


class Solution:
    def maximum69Number (self, num: int) -> int:
        max_digit = -1
        curr_digit = 0
        
        val = num
        while val:
            val, res = divmod(val, 10)
            if res == 6:
                max_digit = curr_digit
            curr_digit += 1
        
        return num if max_digit == -1 else num + 3 * 10 ** max_digit