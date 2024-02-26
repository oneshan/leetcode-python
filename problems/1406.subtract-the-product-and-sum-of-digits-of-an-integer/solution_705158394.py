# 1406 - Subtract the Product and Sum of Digits of an Integer
# Date: 2022-05-23
# Runtime: 30 ms, Memory: 13.9 MB
# Submission Id: 705158394


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        products, sums = 1, 0
        while n > 0:
            digit = n % 10
            n //= 10
            products *= digit
            sums += digit
        return products - sums