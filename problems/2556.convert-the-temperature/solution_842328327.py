# 2556 - Convert the Temperature
# Date: 2022-11-13
# Runtime: 61 ms, Memory: 13.9 MB
# Submission Id: 842328327


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius*1.8 + 32]