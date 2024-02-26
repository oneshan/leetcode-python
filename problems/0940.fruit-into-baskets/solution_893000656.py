# 0940 - Fruit Into Baskets
# Date: 2023-02-07
# Runtime: 955 ms, Memory: 20.1 MB
# Submission Id: 893000656


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = left = 0
        pos = {}
        for right, fruit in enumerate(fruits):
            pos[fruit] = pos.get(fruit, 0) + 1
            while len(pos) == 3:
                pos[fruits[left]] -= 1
                if pos[fruits[left]] == 0:
                    pos.pop(fruits[left])
                left += 1
            ans = max(ans, right-left+1)
        return ans