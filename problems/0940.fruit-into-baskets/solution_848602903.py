# 0940 - Fruit Into Baskets
# Date: 2022-11-23
# Runtime: 2509 ms, Memory: 19.9 MB
# Submission Id: 848602903


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n < 3:
            return n
        
        table = {}
        ans, left = 0, -1
        for right, fruit in enumerate(fruits):
            table[fruit] = right
            if len(table) == 3:
                idx = min(table.values())
                table.pop(fruits[idx])
                left = idx
            ans = max(ans, right-left)
            
        return ans