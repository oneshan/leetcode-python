# 2520 - Using a Robot to Print the Lexicographically Smallest String
# Date: 2024-03-17
# Runtime: 1304 ms, Memory: 19.4 MB
# Submission Id: 1206275032


class Solution:
    def robotWithString(self, s: str) -> str:
        counter = Counter(s)

        ans = []
        stack = []
        for ch in s:
            stack.append(ch)
            counter[ch] -= 1
            if counter[ch] == 0:
                counter.pop(ch)
            
            while counter and stack and min(counter) >= stack[-1]:
                ans.append(stack.pop())
        
        while stack:
            ans.append(stack.pop())

        return ''.join(ans)