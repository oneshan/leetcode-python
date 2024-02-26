# 1584 - Average Salary Excluding the Minimum and Maximum Salary
# Date: 2022-05-22
# Runtime: 58 ms, Memory: 13.9 MB
# Submission Id: 704777907


class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary = min_salary = salary[0]
        total_salary = 0
        for price in salary:
            max_salary = max(price, max_salary)
            min_salary = min(price, min_salary)
            total_salary += price
        
        return (total_salary - max_salary - min_salary) / (len(salary) - 2)