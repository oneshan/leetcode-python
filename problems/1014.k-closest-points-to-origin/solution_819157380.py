# 1014 - K Closest Points to Origin
# Date: 2022-10-10
# Runtime: 1190 ms, Memory: 20.2 MB
# Submission Id: 819157380


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(idx):
            return points[idx][0] ** 2 + points[idx][1] ** 2
        
        def quickselect(left, right):
            # pick pivot at random, swap it to the right
            rand = random.randrange(left, right+1)
            pivot = distance(rand)
            points[rand], points[right] = points[right], points[rand]
            
            # iterate points in the range [left, right)
            p = left
            for i in range(left, right):
                if distance(i) <= pivot:
                    points[p], points[i] = points[i], points[p]
                    p += 1
                    
            # swap our pivot which located in r, to its correct position
            points[p], points[right] = points[right], points[p]
            
            if p > k-1:
                return quickselect(left, p-1)
            if p < k-1:
                return quickselect(p+1, right)
            return points[:k]
        
        return quickselect(0, len(points) - 1) 