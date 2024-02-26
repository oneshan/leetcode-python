# 1205 - Defanging an IP Address
# Date: 2022-11-17
# Runtime: 62 ms, Memory: 13.9 MB
# Submission Id: 845173055


class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ['[.]' if ch == '.' else ch for ch in address]
        return ''.join(ans)