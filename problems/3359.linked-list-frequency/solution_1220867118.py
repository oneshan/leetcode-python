# 3359 - Linked List Frequency
# Date: 2024-04-02
# Runtime: 502 ms, Memory: 37.5 MB
# Submission Id: 1220867118


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = defaultdict(int)
        while head:
            freq[head.val] += 1
            head = head.next
        
        dummy = ListNode()
        curr = dummy
        for val in freq.values():
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next