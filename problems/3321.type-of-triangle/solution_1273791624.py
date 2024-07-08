# 3321 - Type of Triangle
# Date: 2024-06-01
# Runtime: 38 ms, Memory: 16.5 MB
# Submission Id: 1273791624


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        n1 = n2 = n3 = float('-inf')
        for num in nums:
            if num > n1:
                n1, n2, n3 = num, n1, n2
            elif num > n2:
                n2, n3 = num, n2
            else:
                n3 = num

        if (n2 + n3) <= n1:
            return 'none'
        if n1 == n2 == n3:
            return 'equilateral'
        if n1 == n2 or n2 == n3:
            return 'isosceles'
        return 'scalene'