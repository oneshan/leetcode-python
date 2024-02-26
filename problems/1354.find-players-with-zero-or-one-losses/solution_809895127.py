# 1354 - Find Players With Zero or One Losses
# Date: 2022-09-27
# Runtime: 4273 ms, Memory: 68.9 MB
# Submission Id: 809895127


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost = {}
        
        for winner, loser in matches:
            if winner not in lost:
                lost[winner] = 0
            lost[loser] = lost.get(loser, 0) + 1
            
        ans1, ans2 = [], []
        for user, count in lost.items():
            if count == 0:
                ans1.append(user)
            elif count == 1:
                ans2.append(user)

        return [sorted(ans1), sorted(ans2)]