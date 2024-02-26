# 2558 - Minimum Number of Operations to Sort a Binary Tree by Level
# Date: 2022-11-15
# Runtime: 758 ms, Memory: 54.4 MB
# Submission Id: 843891486


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        def swap(arr):
            seen = set()
            n, count = len(arr), 0
            pos = {num: idx for idx, num in enumerate(sorted(arr))}
            for i in range(n):
                cycle = 0
                while i not in seen and i != pos[arr[i]]:
                    seen.add(i)
                    i = pos[arr[i]]
                    cycle += 1
                if cycle:
                    count += cycle - 1
            return count
        
        ans = 0
        queue = deque([root])
        while queue:
            arr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                arr.append(node.val)
            ans += swap(arr)
        return ans