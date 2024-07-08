# 0359 - Logger Rate Limiter
# Date: 2024-05-14
# Runtime: 129 ms, Memory: 22.6 MB
# Submission Id: 1257919154


class Logger:

    def __init__(self):
        self.last_seen = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.last_seen and timestamp - self.last_seen[message] < 10:
            return False
        self.last_seen[message] = timestamp
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)