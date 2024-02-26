# 1512 - Design Underground System
# Date: 2023-05-31
# Runtime: 243 ms, Memory: 26.5 MB
# Submission Id: 960916223


from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.journey = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_t = self.check_in.pop(id)
        self.journey[(start_station, stationName)][0] += (t - start_t)
        self.journey[(start_station, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, count = self.journey[(startStation, endStation)]
        return time / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)