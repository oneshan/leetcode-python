# 0103 - Binary Tree Zigzag Level Order Traversal
# Date: 2024-02-13
# Runtime: 26 ms, Memory: 16.9 MB
# Submission Id: 1173857255


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        flag = 1
        while queue:
            ans.append(deque())
            for _ in range(len(queue)):
                node = queue.popleft()
                if flag:
                    ans[-1].append(node.val)
                else:
                    ans[-1].appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            flag ^= 1
        return ans