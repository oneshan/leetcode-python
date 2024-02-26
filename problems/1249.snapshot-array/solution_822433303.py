# 1249 - Snapshot Array
# Date: 2022-10-15
# Runtime: 1137 ms, Memory: 43.7 MB
# Submission Id: 822433303


class SnapshotArray:
    
    def __init__(self, length: int):
        # map: {index: [(snap_id, val)]}
        self.snap_id = 0
        self.map = {}
        for index in range(length):
            self.map[index] = [[0, 0]]

    def set(self, index: int, val: int) -> None:
        if self.map[index][-1][0] == self.snap_id:
            self.map[index][-1][1] = val
        else:
            self.map[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.map[index]
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid
        return arr[left-1][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)