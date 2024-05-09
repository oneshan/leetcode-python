# 0007 - Reverse Integer
# Date: 2024-05-08
# Runtime: 40 ms, Memory: 16.6 MB
# Submission Id: 1252673515


class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x < 0
        x = abs(x)

        reverse_x = 0
        while x:
            x, digit = divmod(x, 10)
            reverse_x = reverse_x * 10 + digit
        
        if reverse_x + int(not is_neg) > 2 ** 31:
            return 0

        return reverse_x if not is_neg else -reverse_x