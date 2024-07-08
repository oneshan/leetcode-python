# 0090 - Subsets II
# Date: 2024-05-18
# Runtime: 44 ms, Memory: 16.7 MB
# Submission Id: 1261263598


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        def backtrack(arr, i):
            ans.append(arr[:])
            seen = set()
            for j in range(i, n):
                if nums[j] in seen:
                    continue
                seen.add(nums[j])
                arr.append(nums[j])
                backtrack(arr, j+1)
                arr.pop()


        backtrack([], 0)
        return ans