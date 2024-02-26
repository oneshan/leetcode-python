# 1582 - Design Browser History
# Date: 2023-03-18
# Runtime: 277 ms, Memory: 16.8 MB
# Submission Id: 917197383


class ListNode:
    def __init__(self, url=None, prev=None):
        self.url = url
        self.prev = prev
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr.prev and (steps := steps -1) >= 0:
            self.curr = self.curr.prev
        return self.curr.url
        
    def forward(self, steps: int) -> str:
        while self.curr.next and (steps := steps -1) >= 0:
            self.curr = self.curr.next
        return self.curr.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)