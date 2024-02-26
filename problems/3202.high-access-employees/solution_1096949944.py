# 3202 - High-Access Employees
# Date: 2023-11-12
# Runtime: 188 ms, Memory: 16.4 MB
# Submission Id: 1096949944


from collections import defaultdict

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        access = defaultdict(list)
        for user, time_str in access_times:
            tmp = int(time_str)
            time = (tmp // 100) * 60 + (tmp % 100)
            access[user].append(time)
        
        ans = []
        for user, times in access.items():
            if len(times) < 3:
                continue
            count = left = 0
            times.sort()
            for right in range(1, len(times)):
                while left < right and times[right] - times[left] >= 60:
                    left += 1
                count = max(count, right - left + 1)
            if count >= 3:
                ans.append(user)
        return ans