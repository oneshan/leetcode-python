# 1137 - Height Checker
# Date: 2024-06-10
# Runtime: 45 ms, Memory: 16.4 MB
# Submission Id: 1283440556


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = Counter(heights)

        ans = i = 0
        for h in range(1, 101):
            if counter[h] == 0:
                continue
            while counter[h]:
                ans += heights[i] != h
                counter[h] -= 1
                i += 1
        return ans