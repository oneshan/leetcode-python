# 2354 - Minimum Health to Beat Game
# Date: 2023-01-13
# Runtime: 625 ms, Memory: 28.3 MB
# Submission Id: 877419717


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        total = max_damage = 0
        for value in damage:
            total += value
            max_damage = max(max_damage, value)
            
        return 1 + total - min(armor, max_damage)
        