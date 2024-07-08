# 0078 - Subsets
# Date: 2024-05-18
# Runtime: 36 ms, Memory: 16.7 MB
# Submission Id: 1261267273


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        arr = []
        def dfs(i):
            if i == n:
                ans.append(arr[:])
                return

            arr.append(nums[i])
            dfs(i+1)

            arr.pop()
            dfs(i+1)

        dfs(0)
        return ans