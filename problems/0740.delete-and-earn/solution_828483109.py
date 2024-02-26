# 0740 - Delete and Earn
# Date: 2022-10-23
# Runtime: 203 ms, Memory: 16.1 MB
# Submission Id: 828483109


from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        point = defaultdict(int)
        
        max_num = 0
        for num in nums:
            point[num] += num
            max_num = max(max_num, num)
        
        p2 = p1 = 0
        for i in range(max_num+1):
            p2, p1 = p1, max(p2+point[i], p1)
        return p1