# 1072 - Next Greater Node In Linked List
# Date: 2022-10-06
# Runtime: 700 ms, Memory: 19 MB
# Submission Id: 816465771


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack, ans = [], []
        
        idx = 0
        while head:
            ans.append(0)
            while stack and stack[-1][1] < head.val:
                prev_idx, _ = stack.pop()
                ans[prev_idx] = head.val
            stack.append((idx, head.val))
            head = head.next
            idx += 1
            
        return ans