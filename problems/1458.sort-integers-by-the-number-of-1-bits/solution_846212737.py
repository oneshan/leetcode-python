# 1458 - Sort Integers by The Number of 1 Bits
# Date: 2022-11-19
# Runtime: 165 ms, Memory: 14.1 MB
# Submission Id: 846212737


from collections import defaultdict

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_bit(num):
            count = 0
            while num:
                num &= (num-1)
                count += 1
            return count
        
        bits = defaultdict(list)
        for num in arr:
            bits[count_bit(num)].append(num)
        
        ans = []
        for i in range(15):
            ans.extend(sorted(bits[i]))
        return ans