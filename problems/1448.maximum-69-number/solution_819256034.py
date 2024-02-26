# 1448 - Maximum 69 Number
# Date: 2022-10-10
# Runtime: 48 ms, Memory: 13.8 MB
# Submission Id: 819256034


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