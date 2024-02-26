# 1651 - Shuffle String
# Date: 2022-11-22
# Runtime: 123 ms, Memory: 13.9 MB
# Submission Id: 848016231


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [None] * len(s)
        for idx, ch in enumerate(s):
            ans[indices[idx]] = ch
        return ''.join(ans)