# 0291 - Word Pattern II
# Date: 2024-05-31
# Runtime: 31 ms, Memory: 16.4 MB
# Submission Id: 1272586935


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        len_p, len_s = len(pattern), len(s)
        p2s = {}
        s2p = {}

        def backtrack(i, pi):
            if i == len_s and pi == len_p:
                return True
            if i == len_s or pi == len_p:
                return False

            if pattern[pi] in p2s:
                word = p2s[pattern[pi]]
                return s[i:i+len(word)] == word and backtrack(i+len(word), pi+1)

            res = False
            for j in range(i, len_s):
                word = s[i:j+1]
                if word in s2p and s2p[word] != pattern[pi]:
                    continue
                p2s[pattern[pi]] = word
                s2p[word] = pattern[pi]
                res |= backtrack(j+1, pi+1)
                p2s.pop(pattern[pi])
                s2p.pop(word)
            return res

        return backtrack(0, 0)