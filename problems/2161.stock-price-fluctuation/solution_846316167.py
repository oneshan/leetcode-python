# 2161 - Stock Price Fluctuation 
# Date: 2022-11-19
# Runtime: 2022 ms, Memory: 61 MB
# Submission Id: 846316167


from collections import deque

class StockPrice:

    def __init__(self):
        self.mapping = {}
        self.latest_ts = -1
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.mapping[timestamp] = price
        self.latest_ts = max(self.latest_ts, timestamp)
        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))
        

    def current(self) -> int:
        return self.mapping[self.latest_ts]
        
    def maximum(self) -> int:
        price, ts = self.max_heap[0]
        while -price != self.mapping[ts]:
            heapq.heappop(self.max_heap)
            price, ts = self.max_heap[0]
        return -price

    def minimum(self) -> int:
        price, ts = self.min_heap[0]
        while price != self.mapping[ts]:
            heapq.heappop(self.min_heap)
            price, ts = self.min_heap[0]
        return price



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()