# 1461 - Count All Valid Pickup and Delivery Options
# Date: 2023-09-10
# Runtime: 49 ms, Memory: 16.3 MB
# Submission Id: 1045596256


class Solution:
    def countOrders(self, n: int) -> int:
        mod = 1_000_000_007
        
        ans = 1
        for i in range(1, 2*n+1):
            ans *= i
            if i & 1 == 0:
                ans //= 2
            ans %= mod
        
        return ans