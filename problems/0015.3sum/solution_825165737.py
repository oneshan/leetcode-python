# 0015 - 3Sum
# Date: 2022-10-18
# Runtime: 2256 ms, Memory: 18.6 MB
# Submission Id: 825165737


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, unique = set(), set()
        seen = {}
        for i in range(len(nums)):
            if nums[i] in unique:
                continue
            unique.add(nums[i])
            for j in range(i+1, len(nums)):
                complement = -nums[i]-nums[j]
                if complement in seen and seen[complement] == i:
                    ans.add(tuple(sorted((nums[i], nums[j], complement))))
                seen[nums[j]] = i
        return ans