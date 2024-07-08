# 0090 - Subsets II
# Date: 2024-05-18
# Runtime: 39 ms, Memory: 16.8 MB
# Submission Id: 1261276713


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        def backtrack(arr, i):
            if i == n:
                ans.append(arr[:])
                return
            
            arr.append(nums[i])
            backtrack(arr, i+1)
            arr.pop()

            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(arr, i+1)


        backtrack([], 0)
        return ans