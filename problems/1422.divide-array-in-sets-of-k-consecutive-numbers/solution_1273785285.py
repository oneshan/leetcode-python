# 1422 - Divide Array in Sets of K Consecutive Numbers
# Date: 2024-06-01
# Runtime: 350 ms, Memory: 33.8 MB
# Submission Id: 1273785285


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False

        counter = Counter(nums)
        for num in sorted(counter):
            if counter[num] == 0:
                continue
            val = counter[num]
            for i in range(k):
                counter[num+i] -= val
                if counter[num+i] < 0:
                    return False
        return True