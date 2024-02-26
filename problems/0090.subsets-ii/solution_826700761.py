# 0090 - Subsets II
# Date: 2022-10-20
# Runtime: 75 ms, Memory: 14.1 MB
# Submission Id: 826700761


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        
        seen = set()
        ans = []
        for i in range(1<<n):
            curr_sub = [nums[j] for j in range(n) if i & (1 << j) == 0]
            hashcode = ''.join(map(str, curr_sub))
            if hashcode not in seen:
                seen.add(hashcode)
                ans.append(curr_sub)
        
        return ans