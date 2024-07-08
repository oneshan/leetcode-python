# 0853 - Most Profit Assigning Work
# Date: 2024-06-18
# Runtime: 399 ms, Memory: 18.9 MB
# Submission Id: 1292026776


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        jobs = [(d, p) for d, p in zip(difficulty, profit)]
        jobs.sort()
        i, n = 0, len(jobs)

        curr_max = ans = 0
        heapq.heapify(worker)
        while worker:
            w = heapq.heappop(worker)
            while i < n and w >= jobs[i][0]:
                curr_max = max(curr_max, jobs[i][1])
                i += 1
            ans += curr_max

        return ans