# 2107 - Find Unique Binary String
# Date: 2023-11-16
# Runtime: 49 ms, Memory: 16.3 MB
# Submission Id: 1100027368


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        n = len(nums)
        for i in range(n):
            ans.append("1" if nums[i][i] == "0" else "0")
        return ''.join(ans)