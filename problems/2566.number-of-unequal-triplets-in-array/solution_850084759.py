# 2566 - Number of Unequal Triplets in Array
# Date: 2022-11-26
# Runtime: 65 ms, Memory: 13.8 MB
# Submission Id: 850084759


from collections import Counter

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        counter = Counter(nums)
        
        ans, prev, nxt = 0, 0, len(nums)
        for curr in counter.values():
            nxt -= curr
            ans += prev  * curr * nxt
            prev += curr
        return ans