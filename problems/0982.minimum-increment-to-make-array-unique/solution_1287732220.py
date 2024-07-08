# 0982 - Minimum Increment to Make Array Unique
# Date: 2024-06-14
# Runtime: 624 ms, Memory: 34.2 MB
# Submission Id: 1287732220


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        ans = curr = 0
        for i in range(min(counter), max(counter)+1):
            ans += curr
            if counter[i] == 0:
                curr = max(0, curr-1)
            else:
                curr += counter[i] - 1

        while curr:
            ans += curr
            curr -= 1

        return ans