# 2567 - Closest Nodes Queries in a Binary Search Tree
# Date: 2022-11-26
# Runtime: 6150 ms, Memory: 154.5 MB
# Submission Id: 850087861


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        
        # build list
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
            
        inorder(root)
        n = len(arr)
        
        ans = [None] * len(queries)
        for idx, query in enumerate(queries):
            curr_min, curr_max = float('inf'), -1
            left, right = 0, n-1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == query:
                    left = right = mid
                    break
                if arr[mid] > query:
                    right = mid-1
                else:
                    left = mid+1
            ans[idx] = [arr[right] if right >= 0 else -1, arr[left] if left < n else -1]
        return ans