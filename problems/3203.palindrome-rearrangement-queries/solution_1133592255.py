# 3203 - Palindrome Rearrangement Queries
# Date: 2024-01-01
# Runtime: 1924 ms, Memory: 70.6 MB
# Submission Id: 1133592255


class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:

        n = len(s)
        m = n // 2
        
        # prefix sum (diff chars)
        psd = [0]
        for i in range(m):
            psd.append(psd[-1] + (s[i] != s[-i-1]))
    
        # prefix sum (counter)
        counter = [0] * 26
        psc = [counter[:]]
        for c in s:
            counter[ord(c) - ord('a')] += 1
            psc.append(counter[:])

        def check(a1, b1, c1, d1):
            b1 += 1
            d1 += 1
            a2, b2, c2, d2 = n-a1, n-b1, n-c1, n-d1

            # no difference allowed outside the query ranges
            if (min(a1, d2) and psd[min(a1, d2)]
                or m > max(b1, c2) and psd[m] - psd[max(b1, c2)]
                or d2 > b1 and psd[d2] - psd[b1]
                or a1 > c2 and psd[a1] - psd[c2]
               ):
                return False
            
            # intersection of query ranges in the lower half must equate to that in the upper half
            ix1 = [psc[d1][i] - psc[c1][i] for i in range(26)]
            ix2 = [psc[b1][i] - psc[a1][i] for i in range(26)]
            if a1 > d2:
                ix1 = [ix1[i] - (psc[min(a1, c2)][i] - psc[d2][i]) for i in range(26)]
            if c2 > b1:
                ix1 = [ix1[i] - (psc[c2][i] - psc[max(b1, d2)][i]) for i in range(26)]
            if c1 > b2:
                ix2 = [ix2[i] - (psc[min(c1, a2)][i] - psc[b2][i]) for i in range(26)]
            if a2 > d1:
                ix2 = [ix2[i] - (psc[a2][i] - psc[max(d1, b2)][i]) for i in range(26)]
            return all(x >= 0 for x in ix1) and all(x >= 0 for x in ix2) and ix1 == ix2

        return [check(*query) for query in queries]