# 1584 - Average Salary Excluding the Minimum and Maximum Salary
# Date: 2023-05-01
# Runtime: 56 ms, Memory: 16.2 MB
# Submission Id: 942514188


class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        min_s, max_s = float('inf'), float('-inf')
        total = 0
        for s in salary:
            min_s = min(min_s, s)
            max_s = max(max_s, s)
            total += s
            
        return (total - min_s - max_s) / (n-2)