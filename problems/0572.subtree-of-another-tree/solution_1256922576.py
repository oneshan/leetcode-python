# 0572 - Subtree of Another Tree
# Date: 2024-05-13
# Runtime: 53 ms, Memory: 17 MB
# Submission Id: 1256922576


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def to_str(node):
            stack = [node]
            res = []
            while stack:
                node = stack.pop()
                if not node:
                    res.append('#')
                    continue
                res.append(f'^{node.val}')
                stack.append(node.left)
                stack.append(node.right)
            return ''.join(res)

        def kmp_search(string, pattern):
            len_s, len_p = len(string), len(pattern)
            lps = [0] * len_p

            # compute prefix
            j = 0
            for i in range(1, len_p):
                while j and pattern[i] != pattern[j]:
                    j = lps[j-1]
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j

            # find pattern
            j = 0
            for i in range(len_s):
                while j and string[i] != pattern[j]:
                    j = lps[j-1]
                if string[i] == pattern[j]:
                    j += 1
                if j == len_p:
                    return True
            return False

        str_r = to_str(root)
        str_s = to_str(subRoot)
        return kmp_search(str_r, str_s)