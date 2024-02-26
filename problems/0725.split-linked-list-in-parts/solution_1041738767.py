# 0725 - Split Linked List in Parts
# Date: 2023-09-06
# Runtime: 41 ms, Memory: 16.6 MB
# Submission Id: 1041738767


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next 
        size, remains = divmod(count, k)
        
        ans = []
        curr = head
        for i in range(k):
            ans.append(curr)
            for _ in range(size+(i < remains)-1):
                curr = curr.next
            if curr:
                curr.next, curr = None, curr.next
        return ans