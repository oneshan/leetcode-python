# 0775 - N-ary Tree Preorder Traversal
# Date: 2022-06-07
# Runtime: 88 ms, Memory: 16 MB
# Submission Id: 716584055


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children[::-1])
        return ans