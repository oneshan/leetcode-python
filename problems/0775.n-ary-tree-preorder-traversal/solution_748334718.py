# 0775 - N-ary Tree Preorder Traversal
# Date: 2022-07-16
# Runtime: 67 ms, Memory: 16 MB
# Submission Id: 748334718


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            stack.extend(node.children[::-1])
            ans.append(node.val)
        return ans