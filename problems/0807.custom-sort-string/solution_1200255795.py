# 0807 - Custom Sort String
# Date: 2024-03-11
# Runtime: 35 ms, Memory: 16.8 MB
# Submission Id: 1200255795


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)

        ans = []
        for ch in order:
            if ch in counter:
                ans.append(ch * counter.pop(ch))
        for ch in counter:
            ans.append(ch * counter[ch])
        return ''.join(ans)