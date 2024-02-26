# 0808 - Number of Matching Subsequences
# Date: 2022-10-14
# Runtime: 1856 ms, Memory: 16.4 MB
# Submission Id: 822162368


from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        heads = defaultdict(list)
        for idx, word in enumerate(words):
            heads[word[0]].append((idx, 0))
        
        ans = 0
        for ch in s:
            ptr_lst = heads[ch][:]
            heads[ch] = []
            for idx_w, idx_c in ptr_lst:
                idx_c += 1
                if idx_c == len(words[idx_w]):
                    ans += 1
                else:
                    next_ch = words[idx_w][idx_c]
                    heads[next_ch].append((idx_w, idx_c))

            if ans == len(words):
                break            

        return ans