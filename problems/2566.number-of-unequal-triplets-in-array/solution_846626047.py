# 2566 - Number of Unequal Triplets in Array
# Date: 2022-11-20
# Runtime: 1204 ms, Memory: 13.8 MB
# Submission Id: 846626047


from collections import defaultdict

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        table = defaultdict(int)
        for num in nums:
            table[num] += 1
            
        if len(table) < 3:
            return 0
    
        lst = list(table.values())
        ans = 0
        n = len(lst)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    ans += lst[i]*lst[j]*lst[k]
        return ans