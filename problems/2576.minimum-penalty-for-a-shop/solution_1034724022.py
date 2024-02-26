# 2576 - Minimum Penalty for a Shop
# Date: 2023-08-29
# Runtime: 125 ms, Memory: 17.3 MB
# Submission Id: 1034724022


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = min_penalty= sum(customer == 'Y' for customer in customers) 
        ans = 0
        for idx, customer in enumerate(customers, 1):
            if customer == 'Y':
                penalty -= 1
            else:
                penalty += 1
            
            if penalty < min_penalty:
                ans, min_penalty = idx, penalty
        return ans