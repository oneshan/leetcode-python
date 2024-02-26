# 1584 - Average Salary Excluding the Minimum and Maximum Salary
# Date: 2022-11-10
# Runtime: 36 ms, Memory: 13.8 MB
# Submission Id: 840177752


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