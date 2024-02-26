# 0382 - Linked List Random Node
# Date: 2023-11-02
# Runtime: 70 ms, Memory: 19.4 MB
# Submission Id: 1089887991


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        

    def getRandom(self) -> int:
        curr = self.head
        scope, res = 1, 0
        while curr:
            if random.random() < 1 / scope:
                res = curr.val
            scope += 1
            curr = curr.next
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()