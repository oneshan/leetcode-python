# 2149 - Remove Colored Pieces if Both Neighbors are the Same Color
# Date: 2023-10-02
# Runtime: 222 ms, Memory: 17.3 MB
# Submission Id: 1064536542


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        countA = countB = 0
        turnsA = turnsB = 0
        for ch in colors:
            if ch == 'A':
                countA += 1
                turnsB += max(0, countB - 2)
                countB = 0
            else:
                countB += 1
                turnsA += max(0, countA - 2)
                countA = 0
        
        turnsA += max(0, countA - 2)
        turnsB += max(0, countB - 2)
        
        return turnsA > turnsB