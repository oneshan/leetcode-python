# 0187 - Repeated DNA Sequences
# Date: 2024-03-07
# Runtime: 69 ms, Memory: 27.5 MB
# Submission Id: 1196293534


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []

        mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        freq = defaultdict(int)
        ans = []
        
        curr = 0
        for i in range(10):
            curr = (curr << 2) | mapping[s[i]]
        freq[curr] += 1

        for i in range(10, n):
            curr = (curr << 2) | mapping[s[i]]
            curr &= ~(3 << (2 * 10))
            freq[curr] += 1
            if freq[curr] == 2:
                ans.append(s[i-9:i+1])
        return ans