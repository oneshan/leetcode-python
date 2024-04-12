# 0740 - Delete and Earn
# Date: 2024-04-11
# Runtime: 66 ms, Memory: 18.6 MB
# Submission Id: 1229209901


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += num

        p2 = p1 = 0
        for num in sorted(counter.keys()):
            if num-1 in counter:
                p2, p1 = p1, max(p2+counter[num], p1)
            else:
                p2, p1 = p1, p1+counter[num]
        return p1