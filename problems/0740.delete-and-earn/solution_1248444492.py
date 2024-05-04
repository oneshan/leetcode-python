# 0740 - Delete and Earn
# Date: 2024-05-03
# Runtime: 76 ms, Memory: 18.8 MB
# Submission Id: 1248444492


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += num

        p2 = p1 = 0
        for i in range(max(counter)+1):
            p2, p1 = p1, max(p1, counter[i+1] + p2)
        return p1