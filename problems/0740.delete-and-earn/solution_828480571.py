# 0740 - Delete and Earn
# Date: 2022-10-23
# Runtime: 524 ms, Memory: 16.2 MB
# Submission Id: 828480571


from collections import defaultdict

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        point = defaultdict(int)
        for num in nums:
            point[num] += num
        
        p2 = p1 = 0
        for i in range(10001):
            p2, p1 = p1, max(p2+point[i], p1)
        return p1