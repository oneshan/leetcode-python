# 0768 - Partition Labels
# Date: 2024-05-24
# Runtime: 49 ms, Memory: 16.5 MB
# Submission Id: 1265958202


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first, last = defaultdict(int), defaultdict(int)
        for idx, ch in enumerate(s):
            if ch not in first:
                first[ch] = idx
            last[ch] = idx

        ans = []
        left = right = -1
        for idx, ch in enumerate(s):
            right = max(right, last[ch])
            if idx == right:
                ans.append(right-left)
                left = right

        return ans