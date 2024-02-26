# 0451 - Sort Characters By Frequency
# Date: 2024-02-07
# Runtime: 47 ms, Memory: 21.6 MB
# Submission Id: 1168373188


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        max_freq = max(counter.values())

        buckets = [[] for _ in range (max_freq+1)]
        for ch, count in counter.items():
            buckets[count].append(ch)
        
        ans = []
        for count in range(max_freq, -1, -1):
            for ch in buckets[count]:
                ans.append(ch * count)
        return ''.join(ans)