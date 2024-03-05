# 0985 - Bag of Tokens
# Date: 2024-03-04
# Runtime: 59 ms, Memory: 16.7 MB
# Submission Id: 1193144853


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        ans = curr = 0
        left, right = 0, len(tokens) - 1
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                curr += 1
                left += 1
            elif curr:
                power += tokens[right]
                curr -= 1
                right -= 1
            else:
                break
            ans = max(ans, curr)
        return ans