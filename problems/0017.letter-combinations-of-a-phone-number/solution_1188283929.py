# 0017 - Letter Combinations of a Phone Number
# Date: 2024-02-28
# Runtime: 34 ms, Memory: 16.5 MB
# Submission Id: 1188283929


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        mapping = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.ans = []
        n = len(digits)

        def backtrack(idx, arr):
            if idx == n:
                self.ans.append(''.join(arr))
                return
            for ch in mapping[digits[idx]]:
                arr.append(ch)
                backtrack(idx+1, arr)
                arr.pop()

        backtrack(0, [])
        return self.ans