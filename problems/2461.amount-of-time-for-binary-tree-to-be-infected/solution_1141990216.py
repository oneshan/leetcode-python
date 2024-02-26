# 2461 - Amount of Time for Binary Tree to Be Infected
# Date: 2024-01-10
# Runtime: 403 ms, Memory: 68.2 MB
# Submission Id: 1141990216


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(set)
        
        stack = [root]
        while stack:
            curr = stack.pop()
            for next_node in (curr.left, curr.right):
                if next_node:
                    graph[curr.val].add(next_node.val)
                    graph[next_node.val].add(curr.val)
                    stack.append(next_node)
        
        ans = -1
        seen = {start}
        queue = deque([start])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for next_node in graph[node]:
                    if next_node not in seen:
                        queue.append(next_node)
                        seen.add(next_node)
            ans += 1
        return ans