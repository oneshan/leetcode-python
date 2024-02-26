# 2362 - Minimum Rounds to Complete All Tasks
# Date: 2023-01-04
# Runtime: 2169 ms, Memory: 28.1 MB
# Submission Id: 871262176


from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        ans = 0
        for count in counter.values():
            if count == 1:
                return -1
            m, r = divmod(count, 3)
            if r == 0:
                ans += m
            else:
                ans += m + 1
        return ans