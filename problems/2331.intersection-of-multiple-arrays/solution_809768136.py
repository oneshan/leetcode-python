# 2331 - Intersection of Multiple Arrays
# Date: 2022-09-27
# Runtime: 71 ms, Memory: 14.3 MB
# Submission Id: 809768136


from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        table = defaultdict(int)
        for num in nums:
            for elem in num:
                table[elem] += 1
        
        ans = [elem for elem in table if table[elem] == len(nums)]
        return sorted(ans)