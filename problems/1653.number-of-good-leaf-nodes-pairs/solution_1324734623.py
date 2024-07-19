# 1653 - Number of Good Leaf Nodes Pairs
# Date: 2024-07-18
# Runtime: 214 ms, Memory: 17.1 MB
# Submission Id: 1324734623


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        graph = defaultdict(list)
        leaves = set()

        # build graph
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                stack.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                stack.append(node.right)
            if not node.left and not node.right:
                leaves.add(node)
        
        # BFS
        ans = 0
        for leaf in leaves:
            queue = deque([leaf])
            seen = {leaf}
            dist = 0
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    if node != leaf and node in leaves and dist <= distance:
                        ans += 1
                    for neighbor in graph[node]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            queue.append(neighbor)

                dist += 1
                if dist > distance:
                    break

        return ans // 2