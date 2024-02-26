# 1406 - Subtract the Product and Sum of Digits of an Integer
# Date: 2022-11-10
# Runtime: 64 ms, Memory: 13.8 MB
# Submission Id: 840748583


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_d, sum_d = 1, 0
        while n:
            n, d = divmod(n, 10)
            product_d *= d
            sum_d += d
        return product_d - sum_d