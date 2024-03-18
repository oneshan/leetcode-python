# 3360 - Minimum Deletions to Make String K-Special
# Date: 2024-03-17
# Runtime: 95 ms, Memory: 17.5 MB
# Submission Id: 1206136897


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freqs = list(Counter(word).values())

        ans = float('inf')
        for left in freqs:
            curr = 0
            for num in freqs:
                if left <= num <= left + k:
                    continue
                if num < left:
                    curr += num
                else:
                    curr += num - left - k
            ans = min(curr, ans)

        return ans        