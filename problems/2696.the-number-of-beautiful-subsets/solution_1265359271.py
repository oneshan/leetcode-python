# 2696 - The Number of Beautiful Subsets
# Date: 2024-05-23
# Runtime: 2051 ms, Memory: 16.7 MB
# Submission Id: 1265359271


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        self.ans = 0

        def backtrack(arr, i):
            self.ans += 1
            for j in range(i, n):
                if (nums[j] - k) in arr:
                    continue
                arr.append(nums[j])
                backtrack(arr, j+1)
                arr.pop()

        backtrack([], 0)
        return self.ans - 1