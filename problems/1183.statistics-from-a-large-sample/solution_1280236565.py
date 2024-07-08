# 1183 - Statistics from a Large Sample
# Date: 2024-06-07
# Runtime: 54 ms, Memory: 16.6 MB
# Submission Id: 1280236565


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = next(i for i in range(256) if count[i])
        maximum = next(i for i in range(255, -1, -1) if count[i])
        mode = count.index(max(count))

        total_sum = sum (i * num for i, num in enumerate(count))
        total_cnt = sum(count)
        mean = total_sum / total_cnt
        
        for i in range(1, 256):
            count[i] += count[i-1]
        median1 = bisect.bisect(count, (total_cnt-1)/2)
        median2 = bisect.bisect(count, total_cnt/2)
        median = (median1 + median2) / 2.0

        return [minimum, maximum, mean, median, mode]