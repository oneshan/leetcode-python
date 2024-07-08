# 0330 - Patching Array
# Date: 2024-06-16
# Runtime: 57 ms, Memory: 16.7 MB
# Submission Id: 1289850208


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        ans = curr = 0

        for num in nums:
            while curr < n and curr < num-1:
                curr = curr * 2 + 1
                ans += 1
            curr += num
            if curr > n:
                break

        while curr < n:
            curr = curr * 2 + 1
            ans += 1

        return ans