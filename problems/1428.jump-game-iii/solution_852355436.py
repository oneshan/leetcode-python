# 1428 - Jump Game III
# Date: 2022-11-30
# Runtime: 394 ms, Memory: 20.7 MB
# Submission Id: 852355436


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        stack = [start]
        while stack:
            node = stack.pop()
            if arr[node] == 0:
                return True
            if arr[node] < 0:
                continue
            
            for nxt in (node+arr[node], node-arr[node]):
                if 0 <= nxt < n:
                    stack.append(nxt)
            arr[node] = -arr[node]
        return False