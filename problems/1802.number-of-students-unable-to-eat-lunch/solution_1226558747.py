# 1802 - Number of Students Unable to Eat Lunch
# Date: 2024-04-08
# Runtime: 46 ms, Memory: 16.6 MB
# Submission Id: 1226558747


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = Counter(students)
        for s in sandwiches:
            if counter[s] == 0:
                break
            counter[s] -= 1
        return sum(counter.values())