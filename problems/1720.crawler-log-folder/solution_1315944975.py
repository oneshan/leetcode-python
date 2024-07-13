# 1720 - Crawler Log Folder
# Date: 2024-07-10
# Runtime: 51 ms, Memory: 16.8 MB
# Submission Id: 1315944975


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == './':
                continue
            if log == '../':
                ans = max(ans-1, 0)
            else:
                ans += 1
        return ans