# 0217 - Contains Duplicate
# Date: 2022-11-03
# Runtime: 953 ms, Memory: 26.1 MB
# Submission Id: 835898247


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen: return True
            seen.add(num)
        return False