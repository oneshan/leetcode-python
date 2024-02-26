# 0444 - Sequence Reconstruction
# Date: 2023-09-24
# Runtime: 331 ms, Memory: 21.2 MB
# Submission Id: 1057938235


from collections import defaultdict, deque

class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        graph = defaultdict(list)
        indegree = [0] * (n+1)
        
        for seq in sequences:
            for i in range(1, len(seq)):
                _from, _to = seq[i-1], seq[i]
                graph[_from].append(_to)
                indegree[_to] += 1
                
        queue = deque([i for i in range(1, n+1) if indegree[i] == 0])
        ans = []
        
        while queue:
            if len(queue) > 1:
                return False
            node = queue.popleft()
            ans.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return ans == nums
