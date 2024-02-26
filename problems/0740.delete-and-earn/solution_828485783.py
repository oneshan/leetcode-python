# 0740 - Delete and Earn
# Date: 2022-10-23
# Runtime: 228 ms, Memory: 15.9 MB
# Submission Id: 828485783


from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        point = defaultdict(int)
        
        max_num = 0
        for num in nums:
            point[num] += num
            max_num = max(max_num, num)
        
        sorted_key = sorted(point.keys())
        p2 = p1 = 0
        for p in sorted_key:
            if p-1 in point:
                p2, p1 = p1, max(p2+point[p], p1)
            else:
                p2, p1 = p1, p1+point[p]
            
        return p1