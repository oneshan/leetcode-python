# 0679 - 24 Game
# Date: 2023-10-30
# Runtime: 67 ms, Memory: 16.3 MB
# Submission Id: 1087518007


from itertools import permutations

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
        def dfs(cards):
            if len(cards) == 1:
                return abs(cards[0] - 24) < 0.001
            
            for i in range(len(cards) - 1):
                for j in range(i + 1, len(cards)):
                    new_cards = [val for idx, val in enumerate(cards) if idx != i and idx != j]
                    for num in operation(cards[i], cards[j]):
                        new_cards.append(num)
                        if dfs(new_cards):
                            return True
                        new_cards.pop()
            return False
        
        def operation(x, y):
            ans = [x + y, x - y, y - x, x * y]
            if x:
                ans.append(y / x)
            if y:
                ans.append(x / y)
            return ans
        
        return dfs(cards)