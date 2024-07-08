# 0692 - Top K Frequent Words
# Date: 2024-06-16
# Runtime: 42 ms, Memory: 16.8 MB
# Submission Id: 1290149632


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        arr = [(-freq, word) for word, freq in counter.items()]
        heapq.heapify(arr)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(arr)[1])
        return ans