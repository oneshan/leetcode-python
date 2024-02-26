# 0940 - Fruit Into Baskets
# Date: 2022-11-23
# Runtime: 1031 ms, Memory: 20.4 MB
# Submission Id: 848604978


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n < 3:
            return n
        
        table = {}
        ans = left = 0
        for right, fruit in enumerate(fruits):
            table[fruit] = table.get(fruit, 0) + 1
            while len(table) == 3:
                table[fruits[left]] -= 1
                if table[fruits[left]] == 0:
                    del table[fruits[left]]
                left += 1
            ans = max(ans, right-left+1)
            
        return ans