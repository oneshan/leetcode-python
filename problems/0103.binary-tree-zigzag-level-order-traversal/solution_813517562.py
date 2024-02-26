# 0103 - Binary Tree Zigzag Level Order Traversal
# Date: 2022-10-02
# Runtime: 58 ms, Memory: 14.3 MB
# Submission Id: 813517562


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
            ans.append(deque())
            level_nodes = len(queue)
            for _ in range(level_nodes):
                node = queue.popleft()
                if flag:
                    ans[-1].append(node.val)
                else:
                    ans[-1].appendleft(node.val)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)                    
            flag = not flag
        
        return ans