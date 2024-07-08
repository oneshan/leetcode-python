# 0158 - Read N Characters Given read4 II - Call Multiple Times
# Date: 2024-06-19
# Runtime: 43 ms, Memory: 16.5 MB
# Submission Id: 1292579756


# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.queue = deque()

    def read(self, buf: List[str], n: int) -> int:
        size = 0
        while self.queue and size < n:
            buf[size] = self.queue.popleft()
            size += 1

        buf4 = [None] * 4
        for i in range(size, n, 4):
            cnt = read4(buf4)
            for j in range(cnt):
                if i+j < n:
                    buf[i+j] = buf4[j]
                else:
                    self.queue.append(buf4[j])
            size += cnt
            if cnt < 4:
                break
        
        return min(n, size)