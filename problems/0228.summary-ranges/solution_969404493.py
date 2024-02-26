# 0228 - Summary Ranges
# Date: 2023-06-12
# Runtime: 51 ms, Memory: 16.3 MB
# Submission Id: 969404493


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        p1, p2, n = 0, 1, len(nums)
        while p1 < n:
            while p2 < n and nums[p2] == nums[p2-1] + 1:
                p2 += 1
            if p2 == p1 + 1:
                ans.append(str(nums[p1]))
            else:
                ans.append(f'{nums[p1]}->{nums[p2-1]}')
            p1, p2 = p2, p2+1
        return ans
