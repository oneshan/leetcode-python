# 1137 - Height Checker
# Date: 2024-06-10
# Runtime: 45 ms, Memory: 16.6 MB
# Submission Id: 1283441663


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = Counter(heights)

        ans = 0
        h = 1
        for height in heights:
            while counter[h] == 0:
                h += 1
            ans += height != h
            counter[h] -= 1
            
        return ans