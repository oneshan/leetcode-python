# 3303 - Find Beautiful Indices in the Given Array II
# Date: 2024-01-14
# Runtime: 839 ms, Memory: 53.2 MB
# Submission Id: 1145533554


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        
        def kmp_search(string, pattern):
            len_s, len_p = len(string), len(pattern)
            res = []
            lps = [0] * len_p

            # compute prefix
            j = 0
            for i in range(1, len_p):
                while j and pattern[i] != pattern[j]:
                    j = lps[j-1]
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j

            # find pattern
            j = 0
            for i in range(len_s):
                while j and string[i] != pattern[j]:
                    j = lps[j-1]
                if string[i] == pattern[j]:
                    j += 1
                if j == len_p:
                    res.append(i-j+1)
                    j = lps[j-1]
            return res
        
        lst_i = kmp_search(s, a)
        lst_j = kmp_search(s, b)
        
        ans = []
        ptr_j = 0
        for i in lst_i:
            while ptr_j < len(lst_j) and lst_j[ptr_j] < i-k:
                ptr_j += 1
            if ptr_j == len(lst_j):
                break
                
            if abs(lst_j[ptr_j] - i) <= k:
                ans.append(i)
        
        return ans