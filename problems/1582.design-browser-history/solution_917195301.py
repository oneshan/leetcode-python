# 1582 - Design Browser History
# Date: 2023-03-18
# Runtime: 209 ms, Memory: 16.8 MB
# Submission Id: 917195301


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.max_idx = self.curr_idx = 0

    def visit(self, url: str) -> None:
        self.max_idx = self.curr_idx = self.curr_idx + 1
        if len(self.history) <= self.curr_idx:
            self.history.append(url)
        else:
            self.history[self.curr_idx] = url

    def back(self, steps: int) -> str:
        self.curr_idx = max(0, self.curr_idx - steps)
        return self.history[self.curr_idx]
        
    def forward(self, steps: int) -> str:
        self.curr_idx = min(self.max_idx, self.curr_idx + steps)
        return self.history[self.curr_idx]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)