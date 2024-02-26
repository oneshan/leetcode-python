# 1137 - Height Checker
# Date: 2022-11-26
# Runtime: 89 ms, Memory: 13.9 MB
# Submission Id: 850098517


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        bucket = [0] * 101
        for h in heights:
            bucket[h] += 1
        
        ans = b_idx = 0
        for h in heights:
            while not bucket[b_idx]:
                b_idx += 1
            if h != b_idx:
                ans += 1
            bucket[b_idx] -= 1

        return ans