# 0017 - Letter Combinations of a Phone Number
# Date: 2022-10-19
# Runtime: 52 ms, Memory: 13.9 MB
# Submission Id: 825914933


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ans = []
        n = len(digits)
        
        def generate(curr, idx):
            if idx == n:
                ans.append(curr)
                return
            candidates = mapping[digits[idx]]
            for ch in candidates:
                generate(curr+ch, idx+1)
                
        generate('', 0)
        return ans