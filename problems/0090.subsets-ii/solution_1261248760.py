# 0090 - Subsets II
# Date: 2024-05-18
# Runtime: 40 ms, Memory: 16.7 MB
# Submission Id: 1261248760


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        def backtrack(arr, i):
            ans.append(arr[:])
            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                arr.append(nums[j])
                backtrack(arr, j+1)
                arr.pop()


        backtrack([], 0)
        return ans