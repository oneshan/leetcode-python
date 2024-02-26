# 1421 - Find Numbers with Even Number of Digits
# Date: 2022-09-14
# Runtime: 119 ms, Memory: 13.9 MB
# Submission Id: 799532202


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def is_event_digits(n):
            count = 0
            while n:
                n //= 10
                count += 1
            return count & 1 == 0
        
        return sum(is_event_digits(num) for num in nums)