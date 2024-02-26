# 0338 - Counting Bits
# Date: 2022-10-15
# Runtime: 131 ms, Memory: 20.7 MB
# Submission Id: 822757162


class Solution:
    def countBits(self, n: int) -> List[int]:
        step = n.bit_length()
        
        ans = [0]
        for i in range(step-1):
            ans += [c+1 for c in ans]
        
        ans += [ans[c]+1 for c in range(n-len(ans)+1)]
        return ans
    
    