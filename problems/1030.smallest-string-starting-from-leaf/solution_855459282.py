# 1030 - Smallest String Starting From Leaf
# Date: 2022-12-06
# Runtime: 105 ms, Memory: 15.7 MB
# Submission Id: 855459282


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = None
        if not root:
            return ''
        
        def backtracking(node, path):
            nonlocal ans
            
            if not node.left and not node.right:
                if not ans:
                    ans = ''.join(path[::-1])
                else:
                    ans = min(ans, ''.join(path[::-1]))
            
            if node.left:
                path.append(chr(97+node.left.val))
                backtracking(node.left, path)
                path.pop()

            if node.right:
                path.append(chr(97+node.right.val))
                backtracking(node.right, path)
                path.pop()
                
        backtracking(root, [chr(97+root.val)])
        return ans