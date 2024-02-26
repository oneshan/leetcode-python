# 0247 - Strobogrammatic Number II
# Date: 2022-10-19
# Runtime: 174 ms, Memory: 25.4 MB
# Submission Id: 825926304


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        candidates = [
            ('1', '1'),
            ('0', '0'),
            ('8', '8'),
            ('6', '9'),
            ('9', '6'),
        ]
        if n == 1:
            return ["0","1","8"]
        
        def generate(n):
            if n == 0:
                return [""]
            if n == 1:
                return ["0","1","8"]
            
            results = []
            for substring in generate(n-2):
                for x, y in candidates:
                    results.append(x+substring+y)
            return results
        
        ans = []
        for substring in generate(n-2): 
            for x, y in candidates:
                if x != '0':
                    ans.append(x+substring+y)
        return ans