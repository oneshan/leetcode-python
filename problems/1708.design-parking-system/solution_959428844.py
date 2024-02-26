# 1708 - Design Parking System
# Date: 2023-05-29
# Runtime: 133 ms, Memory: 16.8 MB
# Submission Id: 959428844


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = {
            1: big,
            2: medium,
            3: small
        }

    def addCar(self, carType: int) -> bool:
        if self.slots[carType] == 0:
            return False
        self.slots[carType] -= 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)