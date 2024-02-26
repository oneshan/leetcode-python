# 0217 - Contains Duplicate
# Date: 2022-05-22
# Runtime: 479 ms, Memory: 25.9 MB
# Submission Id: 704779419


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False