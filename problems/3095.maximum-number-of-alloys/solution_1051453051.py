# 3095 - Maximum Number of Alloys
# Date: 2023-09-17
# Runtime: 359 ms, Memory: 16.7 MB
# Submission Id: 1051453051


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        
        def calculate(comp):
            nonlocal ans
            left, right = ans, 1000_000_000
            while left <= right:
                mid = (left + right) // 2
                if not check(comp, mid):
                    right = mid - 1
                else:
                    left = mid + 1
            return left - 1
            
        def check(comp, alloyes):
            spend = 0
            for i in range(n):
                spend += max(0, comp[i] * alloyes - stock[i]) * cost[i]
                if spend > budget:
                    return False
            return True
        
        ans = 0
        for i in range(k):
            ans = max(ans, calculate(composition[i]))
            
        return ans