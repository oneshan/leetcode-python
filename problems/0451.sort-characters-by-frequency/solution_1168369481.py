# 0451 - Sort Characters By Frequency
# Date: 2024-02-07
# Runtime: 43 ms, Memory: 17.9 MB
# Submission Id: 1168369481


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        arr = sorted([(count, ch) for ch, count in counter.items()], reverse=True)
        ans = []
        for count, ch in arr:
            ans.append(ch * count)
        return ''.join(ans)