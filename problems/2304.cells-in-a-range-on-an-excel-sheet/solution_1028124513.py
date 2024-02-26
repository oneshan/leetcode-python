# 2304 - Cells in a Range on an Excel Sheet
# Date: 2023-08-22
# Runtime: 54 ms, Memory: 16.4 MB
# Submission Id: 1028124513


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        for i in range(ord(s[0]), ord(s[3])+1):
            ch = chr(i)
            for j in range(int(s[1]), int(s[4])+1):
                ans.append(f'{ch}{j}')
        return ans