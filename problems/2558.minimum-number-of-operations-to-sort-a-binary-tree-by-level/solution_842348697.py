# 2558 - Minimum Number of Operations to Sort a Binary Tree by Level
# Date: 2022-11-13
# Runtime: 2096 ms, Memory: 54.6 MB
# Submission Id: 842348697


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
            arrpos = [*enumerate(arr)]
            arrpos.sort(key = lambda it : it[1])
            for i in range(n):
                if i in seen and arrpos[i][0] == i:
                    continue
                cycle = 0
                j = i
                while j not in seen:
                    seen.add(j)
                    j = arrpos[j][0]
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