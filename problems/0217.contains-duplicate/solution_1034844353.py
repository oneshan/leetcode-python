# 0217 - Contains Duplicate
# Date: 2023-08-29
# Runtime: 474 ms, Memory: 31 MB
# Submission Id: 1034844353


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False