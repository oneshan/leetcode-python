# 0940 - Fruit Into Baskets
# Date: 2024-03-29
# Runtime: 764 ms, Memory: 23.7 MB
# Submission Id: 1217569598


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = Counter()
        left = ans = 0
        for right, fruit in enumerate(fruits):
            counter[fruit] += 1
            while len(counter) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    counter.pop(fruits[left])
                left += 1
            ans = max(ans, right-left+1)
        return ans