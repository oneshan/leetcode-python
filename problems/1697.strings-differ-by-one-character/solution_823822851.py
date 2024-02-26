# 1697 - Strings Differ by One Character
# Date: 2022-10-17
# Runtime: 1102 ms, Memory: 17.1 MB
# Submission Id: 823822851


class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        n, m = len(dict), len(dict[0])
        table = [0] * n
        mod = 1_0000_0000_007  # prime

        for i in range(n):
            for j in range(m):
                table[i] = (26 * table[i] + (ord(dict[i][j])-97)) % mod
        
        base = 1
        for j in range(m-1,-1,-1):
            seen = set()
            for i in range(n):
                mask = (table[i] - base * (ord(dict[i][j])-97)) % mod
                if mask in seen:
                    return True
                seen.add(mask)
            base = 26 * base % mod
        return False