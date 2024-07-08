# 0047 - Permutations II
# Date: 2024-05-18
# Runtime: 53 ms, Memory: 16.9 MB
# Submission Id: 1261257264


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(arr, mask):
            if len(arr) == n:
                ans.append(arr[:])
                return

            seen = set()
            for i in range(n):
                if nums[i] in seen:
                    continue
                if (1 << i) & mask == 0:
                    seen.add(nums[i])
                    arr.append(nums[i])
                    backtrack(arr, mask | (1 << i))
                    arr.pop()

        backtrack([], 0)
        return ans