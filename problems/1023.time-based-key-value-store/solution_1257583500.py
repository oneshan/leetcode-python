# 1023 - Time Based Key-Value Store
# Date: 2024-05-14
# Runtime: 567 ms, Memory: 73.6 MB
# Submission Id: 1257583500


class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ''
        if self.table[key][0][0] > timestamp:
            return ''

        arr = self.table[key]

        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid

        return arr[left-1][1] if left else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)