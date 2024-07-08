# 2300 - Construct String With Repeat Limit
# Date: 2024-06-16
# Runtime: 279 ms, Memory: 18.9 MB
# Submission Id: 1290173239


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        max_heap = [(-ord(ch), freq) for ch, freq in counter.items()]
        heapq.heapify(max_heap)

        ans = []
        prev = None
        while max_heap:
            ch_ansi, freq = heapq.heappop(max_heap)
            if prev == ch_ansi:
                if not max_heap:
                    break
                next_ch_ansi, next_freq = heapq.heappop(max_heap)
                heapq.heappush(max_heap, (ch_ansi, freq))

                ans.append(chr(-next_ch_ansi))
                if next_freq > 1:
                    heapq.heappush(max_heap, (next_ch_ansi, next_freq-1))
                prev = next_ch_ansi
            else:
                ans.append(chr(-ch_ansi) * min(freq, repeatLimit))
                if freq > repeatLimit:
                    heapq.heappush(max_heap, (ch_ansi, freq-repeatLimit))
                prev = ch_ansi
        
        return ''.join(ans)