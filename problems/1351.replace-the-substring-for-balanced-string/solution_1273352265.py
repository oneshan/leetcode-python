# 1351 - Replace the Substring for Balanced String
# Date: 2024-05-31
# Runtime: 291 ms, Memory: 17.1 MB
# Submission Id: 1273352265


class Solution:
    def balancedString(self, s: str) -> int:
        k = len(s) // 4
        counter = Counter(s)

        if counter['Q'] == counter['W'] == counter['E'] == counter['R']:
            return 0
        
        ans = len(s)
        left = 0
        for right, ch in enumerate(s):
            counter[ch] -= 1
            while all(counter[c] <= k for c in 'QWER'):
                ans = min(ans, right - left + 1)
                counter[s[left]] += 1
                left += 1

        return ans