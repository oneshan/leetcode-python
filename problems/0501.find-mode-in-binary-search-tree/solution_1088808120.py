# 0501 - Find Mode in Binary Search Tree
# Date: 2023-11-01
# Runtime: 44 ms, Memory: 18.4 MB
# Submission Id: 1088808120


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
        
        curr = root
        while curr:
            if curr.left:
                _next = curr.left
                while _next.right:
                    _next = _next.right
                _next.right = curr
                
                left = curr.left
                curr.left = None
                curr = left
            else:
                num = curr.val
                if num == prev:
                    curr_freq += 1
                else:
                    curr_freq, prev = 1, num

                if curr_freq > max_freq:
                    ans = []
                    max_freq = curr_freq
                if curr_freq == max_freq:
                    ans.append(num)
                    
                curr = curr.right
        return ans