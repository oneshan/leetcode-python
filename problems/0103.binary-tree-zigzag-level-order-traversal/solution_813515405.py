# 0103 - Binary Tree Zigzag Level Order Traversal
# Date: 2022-10-02
# Runtime: 71 ms, Memory: 14.2 MB
# Submission Id: 813515405


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
                else:
                    node = queue.pop()
                ans[-1].append(node.val)
                if flag:
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                else:
                    if node.right: queue.appendleft(node.right)
                    if node.left: queue.appendleft(node.left)
            flag = not flag
        
        return ans