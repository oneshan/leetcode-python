# 3368 - Winner of the Linked List Game
# Date: 2024-04-02
# Runtime: 50 ms, Memory: 16.5 MB
# Submission Id: 1220865529


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        score = 0
        p1, p2 = head, head.next
        while True:
            score += 1 if p1.val > p2.val else -1
            if not p2.next:
                break
            p1, p2 = p1.next.next, p2.next.next
        
        if score > 0:
            return 'Even'
        if score < 0:
            return 'Odd'
        return 'Tie'