# 0359 - Logger Rate Limiter
# Date: 2022-07-18
# Runtime: 310 ms, Memory: 20.6 MB
# Submission Id: 750333847


class Logger:

    def __init__(self):
        self.table = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.table and timestamp < self.table[message]:
            return False
        self.table[message] = timestamp + 10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)