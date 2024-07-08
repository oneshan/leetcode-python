# 0690 - Employee Importance
# Date: 2024-06-10
# Runtime: 119 ms, Memory: 17.8 MB
# Submission Id: 1283968264


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        table = {}
        for employee in employees:
            table[employee.id] = employee

        def recur(node):
            if not node:
                return 0
            res = node.importance
            for sub in node.subordinates:
                res += recur(table[sub])
            return res


        return recur(table[id])
        