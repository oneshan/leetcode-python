# 1458 - Sort Integers by The Number of 1 Bits
# Date: 2023-10-30
# Runtime: 63 ms, Memory: 16.2 MB
# Submission Id: 1087315557


from collections import defaultdict

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        table = defaultdict(list)
        
        for num in arr:
            tmp, count = num, 0
            while tmp:
                tmp &= (tmp-1)
                count += 1
            table[count].append(num)
        
        ans = []
        for bit in range(20):
            ans.extend(sorted(table[bit]))
        return ans