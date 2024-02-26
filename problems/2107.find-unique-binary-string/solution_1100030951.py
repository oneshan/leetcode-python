# 2107 - Find Unique Binary String
# Date: 2023-11-16
# Runtime: 40 ms, Memory: 16.4 MB
# Submission Id: 1100030951


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(int(num, 2) for num in nums)
        n = len(nums)
        
        for i in range(n+1):
            if i not in nums:
                ans = bin(i)[2:]
                return ans.rjust(n, '0')
        return ""