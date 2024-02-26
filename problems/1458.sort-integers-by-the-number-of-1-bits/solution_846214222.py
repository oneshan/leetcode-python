# 1458 - Sort Integers by The Number of 1 Bits
# Date: 2022-11-19
# Runtime: 103 ms, Memory: 14 MB
# Submission Id: 846214222


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_bit(num):
            count = 0
            while num:
                num &= (num-1)
                count += 1
            return count
        
        ans = [(count_bit(num), num) for num in arr]
        return [num for _, num in sorted(ans)]