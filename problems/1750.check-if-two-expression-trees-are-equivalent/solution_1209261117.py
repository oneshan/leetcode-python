# 1750 - Check If Two Expression Trees are Equivalent
# Date: 2024-03-20
# Runtime: 290 ms, Memory: 18.5 MB
# Submission Id: 1209261117


# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:

        def recur(node):
            counter = Counter()
            stack = [(node, 1)]
            while stack:
                node, sign = stack.pop()
                if node.val in {'+', '-'}:
                    stack.append((node.left, sign))
                    stack.append((node.right, sign if node.val == '+' else -sign))
                else:
                    counter[node.val] += sign
            return counter

        return recur(root1) == recur(root2)