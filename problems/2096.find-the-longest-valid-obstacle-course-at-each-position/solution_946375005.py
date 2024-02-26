# 2096 - Find the Longest Valid Obstacle Course at Each Position
# Date: 2023-05-08
# Runtime: 1524 ms, Memory: 33.7 MB
# Submission Id: 946375005


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lis = []
        ans = []
        for num in obstacles:
            idx = bisect.bisect_right(lis, num)  
            if idx == len(lis):
                lis.append(num)
            else:
                lis[idx] = num
            ans.append(idx+1)
                
        return ans