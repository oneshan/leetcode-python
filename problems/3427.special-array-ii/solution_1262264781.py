# 3427 - Special Array II
# Date: 2024-05-19
# Runtime: 931 ms, Memory: 55.9 MB
# Submission Id: 1262264781


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        
        prefix = [0] * n
        curr = 0
        for i in range(1, n):
            if nums[i] & 1 != nums[i-1] & 1:
                curr += 1
            prefix[i] = curr
        
        ans = []
        for _from, _to in queries:
            ans.append(prefix[_to] - prefix[_from] == _to - _from)
        return ans