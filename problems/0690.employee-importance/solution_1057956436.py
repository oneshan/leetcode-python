# 0690 - Employee Importance
# Date: 2023-09-24
# Runtime: 125 ms, Memory: 17.7 MB
# Submission Id: 1057956436


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
        table = {e.id: e for e in employees}
        ans = 0
        stack = [id]
        while stack:
            eid = stack.pop()
            ans += table[eid].importance
            for neighbor in table[eid].subordinates:
                stack.append(neighbor)
        return ans