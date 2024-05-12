# 0007 - Reverse Integer
# Date: 2024-05-11
# Runtime: 44 ms, Memory: 16.7 MB
# Submission Id: 1255083332


class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x < 0
        x = abs(x)

        threshold = divmod(2 ** 31 - 1, 10)

        reverse_x = 0
        while x:
            x, digit = divmod(x, 10)
            reverse_x = reverse_x * 10 + digit
            if reverse_x > threshold[0] and x:
                return 0
            if reverse_x == threshold[0] and x + int(not is_neg) >= threshold[1]:
                return 0
        
        return reverse_x if not is_neg else -reverse_x