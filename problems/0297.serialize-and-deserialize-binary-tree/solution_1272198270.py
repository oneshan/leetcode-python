# 0297 - Serialize and Deserialize Binary Tree
# Date: 2024-05-30
# Runtime: 80 ms, Memory: 21 MB
# Submission Id: 1272198270


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        def preorder(node):
            if not node:
                res.append('1001')
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = [int(d) for d in data.split(',')]
        self.idx = 0
        n = len(arr)

        def preorder():
            if arr[self.idx] == 1001:
                self.idx += 1
                return None

            node = TreeNode(arr[self.idx])
            self.idx += 1
            node.left = preorder()
            node.right = preorder()
            return node

        return preorder()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))