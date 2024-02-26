# 0359 - Logger Rate Limiter
# Date: 2022-10-16
# Runtime: 441 ms, Memory: 20.9 MB
# Submission Id: 823549840


from collections import deque

class Logger:

    def __init__(self):
        self._msg_set = set()
        self._msg_queue = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self._msg_queue:
            msg, ts = self._msg_queue[0]
            if timestamp - ts >= 10:
                self._msg_queue.popleft()
                self._msg_set.remove(msg)
            else:
                break
        
        if message not in self._msg_set:
            self._msg_set.add(message)
            self._msg_queue.append((message, timestamp))
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)