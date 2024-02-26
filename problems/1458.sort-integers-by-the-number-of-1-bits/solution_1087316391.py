# 1458 - Sort Integers by The Number of 1 Bits
# Date: 2023-10-30
# Runtime: 69 ms, Memory: 16.5 MB
# Submission Id: 1087316391


from collections import defaultdict

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        lst = []
        
        for num in arr:
            tmp, count = num, 0
            while tmp:
                tmp &= (tmp-1)
                count += 1
            lst.append((count, num))
        
        return [num for _, num in sorted(lst)]