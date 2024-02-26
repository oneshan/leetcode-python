# 1723 - Maximum Number of Achievable Transfer Requests
# Date: 2023-07-02
# Runtime: 1788 ms, Memory: 16.5 MB
# Submission Id: 984115154


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        indegree = [0] * n
        len_r = len(requests)
        
        def backtrack(idx):
            if idx == len_r:
                if min(indegree) == max(indegree) == 0:
                    return 0
                return float('-inf')

            _from, _to = requests[idx]
            indegree[_from] -= 1
            indegree[_to] += 1
            ans = 1 + backtrack(idx+1)
            indegree[_from] += 1
            indegree[_to] -= 1
            return max(ans, backtrack(idx+1))
        
        return backtrack(0)