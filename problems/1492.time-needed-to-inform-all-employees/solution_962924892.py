# 1492 - Time Needed to Inform All Employees
# Date: 2023-06-03
# Runtime: 1294 ms, Memory: 48 MB
# Submission Id: 962924892


from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return 0
        
        children = defaultdict(list)
        cost = {}
        
        for idx, (parent, time) in enumerate(zip(manager, informTime)):
            children[parent].append(idx)
            cost[idx] = time
        
        stack = [(-1, 0)]
        ans = 0
        while stack:
            employee, curr_cost = stack.pop()
            if employee not in children:
                ans = max(ans, curr_cost)
                continue

            for child in children[employee]:
                stack.append((child, curr_cost + cost[child]))
        return ans
        