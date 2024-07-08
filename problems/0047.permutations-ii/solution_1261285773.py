# 0047 - Permutations II
# Date: 2024-05-18
# Runtime: 40 ms, Memory: 17 MB
# Submission Id: 1261285773


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(i):
            if i == n:
                ans.append(nums[:])
                return

            seen = set()
            for j in range(i, n):
                if nums[j] in seen:
                    continue
                seen.add(nums[j])
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]
                
        backtrack(0)
        return ans