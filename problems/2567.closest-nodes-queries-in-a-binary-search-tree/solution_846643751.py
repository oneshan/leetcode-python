# 2567 - Closest Nodes Queries in a Binary Search Tree
# Date: 2022-11-20
# Runtime: 4269 ms, Memory: 74.6 MB
# Submission Id: 846643751


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        
        # build list
        node, output = root, []
        while node:  
            if not node.left: 
                output.append(node.val)
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
                    output.append(node.val)
                    node = node.right
        n = len(output)
        
        ans = [0] * len(queries)
        for idx, query in enumerate(queries):
            curr_min, curr_max = float('inf'), -1
            left, right = 0, n-1
            while left <= right:
                mid = (left + right) // 2
                if output[mid] == query:
                    left = right = mid
                    break
                if output[mid] > query:
                    right = mid-1
                else:
                    left = mid+1
            ans[idx] = [output[right] if right >= 0 else -1, output[left] if left < n else -1]
        return ans