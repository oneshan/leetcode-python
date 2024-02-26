# 0017 - Letter Combinations of a Phone Number
# Date: 2023-09-19
# Runtime: 43 ms, Memory: 16.2 MB
# Submission Id: 1052756815


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
        
        def backtrack(arr, idx):
            if idx == n:
                ans.append(''.join(arr))
                return
            for ch in mapping[digits[idx]]:
                arr.append(ch)
                backtrack(arr, idx + 1)
                arr.pop()
        
        backtrack([], 0)
        return ans
            