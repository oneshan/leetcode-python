# 2149 - Remove Colored Pieces if Both Neighbors are the Same Color
# Date: 2023-10-02
# Runtime: 171 ms, Memory: 17.4 MB
# Submission Id: 1064537982


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        countA = countB = 0
        turnsA = turnsB = 0
        for ch in colors:
            if ch == 'A':
                countA += 1
                countB = 0
            else:
                countB += 1
                countA = 0
            turnsA += 1 if countA > 2 else 0
            turnsB += 1 if countB > 2 else 0
        return turnsA > turnsB