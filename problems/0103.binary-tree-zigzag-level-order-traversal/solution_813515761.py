# 0103 - Binary Tree Zigzag Level Order Traversal
# Date: 2022-10-02
# Runtime: 59 ms, Memory: 14.1 MB
# Submission Id: 813515761


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        flag = 1
        while queue:
            ans.append([])
            level_nodes = len(queue)
            for _ in range(level_nodes):
                if flag:
                    node = queue.popleft()
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)                    
                else:
                    node = queue.pop()
                    if node.right: queue.appendleft(node.right)
                    if node.left: queue.appendleft(node.left)
                ans[-1].append(node.val)
            flag = not flag
        
        return ans