# 0853 - Most Profit Assigning Work
# Date: 2024-06-18
# Runtime: 688 ms, Memory: 19.5 MB
# Submission Id: 1292031978


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_ability = max(worker)
        jobs = [0] * (max_ability + 1)

        for d, p in zip(difficulty, profit):
            if d <= max_ability:
                jobs[d] = max(jobs[d], p)

        for i in range(1, max_ability+1):
            jobs[i] = max(jobs[i], jobs[i-1])

        ans = 0
        for ability in worker:
            ans += jobs[ability]
        return ans