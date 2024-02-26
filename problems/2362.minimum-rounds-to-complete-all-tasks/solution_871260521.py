# 2362 - Minimum Rounds to Complete All Tasks
# Date: 2023-01-04
# Runtime: 2608 ms, Memory: 28.3 MB
# Submission Id: 871260521


from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        ans = 0
        for count in counter.values():
            m, r = divmod(count, 3)
            if r == 0:
                ans += m
            if r == 2:
                ans += m + 1
            if r == 1:
                if m == 0:
                    return -1
                ans += m + 1
        return ans