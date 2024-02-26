# 0501 - Find Mode in Binary Search Tree
# Date: 2023-11-01
# Runtime: 50 ms, Memory: 20.2 MB
# Submission Id: 1088809926


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        curr_freq, max_freq, ans = 0, 0, []
        prev = None
        
        def check(num):
            nonlocal curr_freq, max_freq, ans, prev
            if num == prev:
                curr_freq += 1
            else:
                curr_freq, prev = 1, num

            if curr_freq > max_freq:
                ans = []
                max_freq = curr_freq
            if curr_freq == max_freq:
                ans.append(num)
        
        node = root
        while node:
            if not node.left:
                check(node.val)
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    check(node.val)
                    node = node.right
        return ans