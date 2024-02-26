# 3151 - Minimum Processing Time
# Date: 2023-10-08
# Runtime: 607 ms, Memory: 32.6 MB
# Submission Id: 1069769453


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        n = len(processorTime)
        m = len(tasks)
        
        processorTime.sort()
        tasks.sort(reverse=True)
        
        ans = [0] * n
        j = 0
        for i in range(0, m, 4):
            ans[j % n] += processorTime[j % n] + tasks[i]
            j += 1
        return max(ans)