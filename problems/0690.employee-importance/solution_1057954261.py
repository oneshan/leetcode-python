# 0690 - Employee Importance
# Date: 2023-09-24
# Runtime: 138 ms, Memory: 17.8 MB
# Submission Id: 1057954261


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import defaultdict

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        score = defaultdict(int)
        graph = defaultdict(list)
        for employee in employees:
            score[employee.id] = employee.importance
            graph[employee.id] = employee.subordinates
            
        ans = 0
        stack = [id]
        seen = {id}
        while stack:
            node = stack.pop()
            ans += score[node]
            for neighbor in graph[node]:
                if neighbor not in seen:
                    stack.append(neighbor)
                    seen.add(neighbor)
        return ans