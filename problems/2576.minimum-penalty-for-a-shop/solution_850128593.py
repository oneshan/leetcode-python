# 2576 - Minimum Penalty for a Shop
# Date: 2022-11-26
# Runtime: 165 ms, Memory: 14.8 MB
# Submission Id: 850128593


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        total_y = sum(ch == 'Y' for ch in customers)
        
        min_penalty, min_close = total_y, 0
        penalty = total_y
        for idx, ch in enumerate(customers, 1):
            if ch == 'Y':
                penalty -= 1
            else:
                penalty += 1
            if penalty < min_penalty:
                min_penalty, min_close = penalty, idx
        return min_close