# 0404 - Sum of Left Leaves
# Date: 2022-11-18
# Runtime: 70 ms, Memory: 14.1 MB
# Submission Id: 845735921


class Solution:
    
    def sumOfLeftLeaves(self, root):
        ans, node = 0, root
        while node:
            if not node.left: 
                node = node.right 
            else: 
                prev = node.left 
                if not prev.left and not prev.right:
                    ans += prev.val

                while prev.right and prev.right != node:
                    prev = prev.right
                    
                if prev.right:
                    prev.right = None
                    node = node.right
                else:
                    prev.right = node  
                    node = node.left  
        return ans