# 1275 - Validate Binary Tree Nodes
# Date: 2023-10-17
# Runtime: 311 ms, Memory: 20.4 MB
# Submission Id: 1077190412


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for i in range(n):
            if leftChild[i] != -1:
                graph[i].append(leftChild[i])
                in_degree[leftChild[i]] += 1
            if rightChild[i] != -1:
                graph[i].append(rightChild[i])
                in_degree[rightChild[i]] += 1
        
        root = [i for i in range(n) if in_degree[i] == 0]
        if len(root) != 1:
            return False
        
        root = root[0]
        stack = [root]
        seen = {root}
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor in seen:
                    return False
                stack.append(neighbor)
                seen.add(neighbor)
        return len(seen) == n