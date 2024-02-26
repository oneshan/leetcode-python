# 2567 - Closest Nodes Queries in a Binary Search Tree
# Date: 2022-11-26
# Runtime: 4912 ms, Memory: 157.4 MB
# Submission Id: 850091793


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
        
        def binary_search(query):
            left, right = 0, n-1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == query:
                    return mid
                if arr[mid] > query:
                    right = mid -1
                else:
                    left = mid + 1
            # arr[left-1] < query < arr[left]
            return left
        
        ans = []
        for query in queries:
            idx = binary_search(query)
            if idx == n:
                min_i, max_i = arr[idx-1], -1
            elif arr[idx] == query:
                min_i = max_i = query
            elif idx == 0:
                min_i, max_i = -1, arr[idx]
            else:
                min_i, max_i = arr[idx-1], arr[idx]
            ans.append([min_i, max_i])
        return ans