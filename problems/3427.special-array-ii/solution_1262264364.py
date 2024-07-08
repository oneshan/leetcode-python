# 3427 - Special Array II
# Date: 2024-05-19
# Runtime: 938 ms, Memory: 56 MB
# Submission Id: 1262264364


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        
        prefix = [0] * (n + 1)
        curr = 0
        for i in range(1, n):
            if nums[i] & 1 != nums[i-1] & 1:
                curr += 1
            prefix[i] = curr
        
        ans = []
        for _from, _to in queries:
            ans.append(prefix[_to] - prefix[_from] == _to - _from)
        return ans