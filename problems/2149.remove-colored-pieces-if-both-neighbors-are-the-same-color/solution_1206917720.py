# 2149 - Remove Colored Pieces if Both Neighbors are the Same Color
# Date: 2024-03-18
# Runtime: 158 ms, Memory: 17.5 MB
# Submission Id: 1206917720


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)

        count = 0
        for i in range(2, n):
            if colors[i-2] == colors[i-1] == colors[i]:
                if colors[i] == 'A':
                    count += 1
                else:
                    count -= 1
        return count > 0