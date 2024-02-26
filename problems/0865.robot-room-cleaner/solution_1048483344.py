# 0865 - Robot Room Cleaner
# Date: 2023-09-13
# Runtime: 54 ms, Memory: 18.2 MB
# Submission Id: 1048483344


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        @cache
        def backtrack(x, y, d):
            seen.add((x, y))
            robot.clean()
            
            for i in range(4):
                next_d = (d+i) % 4
                dx, dy = directions[next_d]
                if (x + dx, y + dy) not in seen and robot.move():
                    backtrack(x+dx, y+dy, next_d)
                    go_back()            
                robot.turnRight()
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        seen = set()
        backtrack(0, 0, 0)