# 0359 - Logger Rate Limiter
# Date: 2022-10-16
# Runtime: 178 ms, Memory: 20.9 MB
# Submission Id: 823546683


class Logger:

    def __init__(self):
        self.message = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp >= self.message.get(message, -10) + 10:
            self.message[message] = timestamp
            return True
        return False            


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)