# 0382 - Linked List Random Node
# Date: 2023-03-10
# Runtime: 93 ms, Memory: 17.4 MB
# Submission Id: 912426254


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        scope = 1
        ans = 0
        
        curr = self.head
        while curr:
            if random.random() < 1 / scope:
                ans = curr.val
            curr = curr.next
            scope += 1
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()