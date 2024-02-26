# 2998 -   Count Symmetric Integers
# Date: 2023-09-03
# Runtime: 303 ms, Memory: 16.3 MB
# Submission Id: 1039015395


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        
        def is_symmetric(num):
            if num < 100:
                return num in {11, 22, 33, 44, 55, 66, 77, 88, 99}
            if 100 <= num <= 999:
                return False
            n1, n2 = divmod(num, 100)
            return sum(divmod(n1, 10)) == sum(divmod(n2, 10))
                
        
        while low <= high:
            if is_symmetric(low):
                ans += 1
            low += 1
        return ans